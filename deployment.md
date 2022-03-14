# Deployment - Traditional Hosting


Traditional hosting, means that the application is installed manually or through a scripted installer on a stock server machine. The process involves installing the application, its dependencies a production scale web server and configuring the system so that it is secure.

## Table of contents

<!-- toc -->

- [Operating Systems](#operating-systems)
- [Paid Public Servers](#paid-public-servers)
- [Free Private Server](#free-private-server)
- [SSH](#ssh)
- [Create a new user](#create-a-new-user)
- [Securing Your Server](#securing-your-server)
  * [1. Disable root logins & password logins via SSH](#1-disable-root-logins--password-logins-via-ssh)
  * [2. Install a Firewall](#2-install-a-firewall)
- [Installing Base Dependencies](#installing-base-dependencies)
  * [Postfix](#postfix)
    + [1. Make sure your hostname matches your domain name](#1-make-sure-your-hostname-matches-your-domain-name)
    + [2. Modify the postfix config](#2-modify-the-postfix-config)
    + [3. Having issues?](#3-having-issues)
  * [Elasticsearch](#elasticsearch)
- [Use Git to Install the Application from GitHub](#use-git-to-install-the-application-from-github)
- [Create a Virtual Environment and Install Dependencies](#create-a-virtual-environment-and-install-dependencies)
- [Recreate the .env file](#recreate-the-env-file)
- [Set the FLASK_APP variable](#set-the-flask_app-variable)
- [Compile Translations](#compile-translations)
- [Set up MySQL](#set-up-mysql)
- [Set up Gunicorn and Supervisor](#set-up-gunicorn-and-supervisor)
- [Set up Nginx](#set-up-nginx)
- [Deploying Updates](#deploying-updates)
- [Mapping a Domain to Digital Ocean](#mapping-a-domain-to-digital-ocean)
- [SSL Certificates](#ssl-certificates)
  * [Renewing your SSL certificates](#renewing-your-ssl-certificates)
- [Redis Server & RQ workers](#redis-server--rq-workers)
- [Security](#security)
- [Misc commands](#misc-commands)
- [Troubleshooting lessons learned](#troubleshooting-lessons-learned)

<!-- tocstop -->

## Operating Systems

From a technical point of view, many applications can be deployed on any of the major operating systems, a list which includes a large variety of open-source Linux and BSD distributions, and the commercial OSX and Microsoft Windows. Since OSX and Windows are desktop operating systems that are not optimized to work as servers, it makes more sense to choose between a Linux or a BSD operating system. The most popular of the two is Linux. As far as Linux distributions go, the most popular is Ubuntu.

## Paid Public Servers

For approximately $5-25 per month, the following will rent you a virtualized Linux server:

- [Digital Ocean](https://www.digitalocean.com/) (entry level servers have 1GB of RAM)
- [Linode](https://www.linode.com/pricing) (entry level servers have 1GB of RAM)
- [Amazon Lightsail](https://aws.amazon.com/lightsail/) (entry level servers have 512MB of RAM)
- [Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/)
- [Heroku](https://www.heroku.com/pricing) (has a free hobby tier)
- [Firebase](https://firebase.google.com/pricing) (has a free hobby plan)

## Free Private Server

[Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) are two tools that combined allow you to create a virtual server similar to the paid ones on your own computer. To use these, install both and then create a file named *Vagrantfile* to describe the specs of your virtual machine:

This file configures a Ubuntu 16.04 server with 1GB of RAM, which you will be able to access from the host computer at IP address 192.168.33.10.

```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
end
```

To create the server, run the following command:

```
$ vagrant up
```

For more information see the [vagrant command line documentation](https://www.vagrantup.com/docs/cli/).

## SSH

Most of your interactions with the server will be through SSH. On Linux and Mac OS, OpenSSH is already installed. If you are using a third party virtual server, you'll want to make sure to look into adding your ssh keys so you don't have to enter passwords all the time. On Digital Ocean it's under settings/security.

```
$ ssh root@165.227.40.207
```

If you're using Vagrant VM, you can open a terminal session with this:

```
$ vagrant ssh
```

## Create a new user

If you're using a public virtual server you should create a regular user account to do your deployment work.

```
$ adduser --gecos "" jessica
$ usermod -aG sudo jessica
$ su jessica
```

Now, in a separate terminal session on your local machine, copy your public ssh key using this command:

```
$ cat ~/.ssh/id_rsa.pub
```

Switch back to your remote server:

```
$ mkdir ~/.ssh
$ echo <paste-your-key-here> >> ~/.ssh/authorized_keys
$ chmod 600 ~/.ssh/authorized_keys
```

You should now be able to exit out of SSH and SSH back in again as the new user without entering any passwords.

## Securing Your Server

There are a few steps that you can take, directed at closing a number of potential doors through which an attacker may gain access.

### 1. Disable root logins & password logins via SSH

Since we now have a new user account that can run administrator commands via sudo, there is really no need to expose the root account. To disable root logins, you need to edit the `/etc/ssh/sshd_config` file on your server. You probably have the vim and nano text editors installed in your server to edit files:

```
$ sudo vi /etc/ssh/sshd_config
$ sudo nano /etc/ssh/sshd_config
```

Locate and change the following lines:

```
PermitRootLogin no
PasswordAuthentication no
```

After you are done editing the SSH configuration, the service needs to be restarted for the changes to take effect:

```
$ sudo service ssh restart
```

### 2. Install a Firewall

This is a software that blocks accesses to the server on any ports that are not explicitly enabled. These commands install ufw, the Uncomplicated Firewall, and configure it to only allow external traffic on port 22 (ssh), 80 (http) and 443 (https). Any other ports will not be allowed.

```
$ sudo apt-get install -y ufw
$ sudo ufw allow ssh
$ sudo ufw allow http
$ sudo ufw allow 443/tcp
$ sudo ufw --force enable
$ sudo ufw status
```

## Installing Base Dependencies

As of 2019, Digital Ocean's default Ubuntu is 18.04 and this comes with Python 3.6.7 pre-installed.

Consider the following:

```
$ sudo apt-get -y update
$ sudo apt-get -y install python3 python3-venv python3-dev
$ sudo apt-get -y install postfix supervisor nginx git
$ sudo apt-get -y install mysql-server
$ sudo apt-get -y install sqlite3 libsqlite3-dev
```

- **postfix** - mail transfer agent, for sending out email.
- **supervisor** - a tool to monitor the Flask server process. It automatically restarts it if it ever crashes, or if the server is rebooted.
- **ngnix** - the server that accepts all requests that come from the outside world, and forwards them to the application.
- **git** - to download the application directly from its github repo.
- **mysql-server** - MySQL for the database (for postgreSQL, see [deployment_digitalocean.md](deployment_digitalocean.md)).
- **sqlite3** - dev tools for sqlite3 if you're using that instead.


### Postfix

Note that when you install postfix, a screen will come up where you'll be asked some questions regarding he installation of the postfix package. You can accept these with their default answers.

Note that the default installation of postfix is likely insufficient for sending email in a production environment. To avoid spam and malicious emails, many servers require the sender server to identify itself through security extensions, which means at the very least you have to have a domain name associated with your server. If you want to learn how to fully configure an email server so that it passes standard security tests, see the following Digital Ocean guides:


- [Postfix Configuration](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-16-04)
- [Postfix Configuration updated for Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-on-ubuntu-18-04)
- [Adding an SPF Record](https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability)
- [DKIM Installation and Configuration](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-dkim-with-postfix-on-debian-wheezy)

In addition I've heard it's good to set up DMARC. Here's a couple of links that explain further:

- [How to eliminate spam and protect your name with DMARC](https://www.skelleton.net/2015/03/21/how-to-eliminate-spam-and-protect-your-name-with-dmarc/)
- [What is DMARC?](https://www.proofpoint.com/us/corporate-blog/post/what-is-dmarc)

Some highlights:

#### 1. Make sure your hostname matches your domain name

The instructions say:

> Note that your server's hostname should match this domain or subdomain. You can verify the server's hostname by typing hostname at the command prompt. The output should match the name you gave the Droplet when it was being created.

Just to be safe I make sure my domain name (e.g. `microblog.zebro.id`) matches the hostname in all the following places (I also name my droplet to match my domain name though I don't know if this is necessary):

```
sudo nano /etc/hostname
sudo nano /etc/mailname
sudo nano /etc/hosts
sudo hostname microblog.zebro.id
```

After you do this you should reboot your server:

```
sudo reboot
```

#### 2. Modify the postfix config

> Postfix is set up with a default configuration. If you need to make changes, edit */etc/postfix/main.cf* (and others) as needed. After modifying *main.cf*, be sure to run */etc/init.d/postfix reload*.

```
sudo nano /etc/postfix/main.cf
```

Change the following options like so:

```
myhostname = microblog.zebro.id
inet_interfaces = loopback-only
mydestination = $myhostname, localhost.$mydomain, $mydomain
```

After making changes:

```
/etc/init.d/postfix reload
sudo systemctl restart postfix
```

#### 3. Having issues?

First thing to do is check the log:

```
sudo nano /var/log/mail.log
```

Note that Apple email addresses are a pain in the ass. If an Apple email address is used as the 'sender' (in your actual flask application email functions), you may get blocked by this site called Proof Point. It may also happen if the `to:` address is an Apple email. Proof Point will block your ip. You'll have to go to their site (the address will be in the error logs) and fill out a f***ing form for them to let you send emails.


### Elasticsearch

This service requires a large amount of RAM, so it's only viable if you have a server with more than 2GB of RAM. Note that the Elasticsearch package available in the Ubuntu 16.04 package repository is too old and will not work, you need version 6.x or newer.

First, install Java:

```
$ sudo apt-get update
$ sudo apt-get install default-jdk
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer
```

Then, install Elasticsearch (see their download page for the [most current debian package](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html#install-deb)).

```
$ sudo apt-get update
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.deb
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.deb.sha512
$ shasum -a 512 -c elasticsearch-6.2.4.deb.sha512
$ sudo dpkg -i elasticsearch-6.2.4.deb
$ sudo systemctl enable elasticsearch.service
$ sudo ufw allow from <ip.address> to any port 9200
```

Now edit the config:

```
$ sudo nano /etc/elasticsearch/elasticsearch.yml
```

uncomment the following lines and provide your own names:

```
cluster.name: microblog-cluster
node.name: "My First Node"
network.host: 0.0.0.0
```

This is the bare minimum. For more information, see this tutorial:

- [Install and Configure Elasticsearch on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-16-04)
- [How To Install Elasticsearch, Logstash, and Kibana (Elastic Stack) on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elastic-stack-on-ubuntu-18-04)

Lastly:

```
$ sudo systemctl start elasticsearch
```

Check it:

```
$ service elasticsearch status
$ curl localhost:9200
```

## Use Git to Install the Application from GitHub

You'll need to create a new repo on Github and then push your local repo to it. Once its there you can clone it onto your remote server. First, on your server, make sure you're in your home directory:

```
$ cd ~/
$ git clone https://github.com/username/reponame.git
```

## Create a Virtual Environment and Install Dependencies

This is done in the same way as you would on your local machine:

```
$ cd <reponame>
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
(venv) $ pip install gunicorn pymysql
```

In addition to the requirements we install the *gunicorn* package which is a production web server for Python applications and the *pymysql* package which contains the MySQL driver that enables SQLAlchemy to work with MySQL databases.

## Recreate the .env file

Assuming this file is in the `.gitignore`, we'll need to create it on the server:

```
$ nano .env
```

I've commented out the ELASTICSEARCH_URL for now.

```
SECRET_KEY=<your_secret_key_goes_here>
MAIL_SERVER=localhost
MAIL_PORT=25
DATABASE_URL=mysql+pymysql://microblog:<db-password>@localhost:3306/microblog
MS_TRANSLATOR_KEY=<your_translator_key_here>
# ELASTICSEARCH_URL=http://localhost:9200
```

## Set the FLASK_APP variable

Normally we would have to manually set (export) the FLASK_APP environment variable each time we log in but... we can have it set automatically every time we log in by adding it to the ~/.profile for the user account.

```
$ echo "export FLASK_APP=microblog.py" >> ~/.profile
```

Log out and then log back in to have it set. You can check by running the `printenv` command.

## Compile Translations

Provided the FLASK_APP is now set, you should be able to run the translations compiler if you're using that stuff in your app:

```
(venv) $ flask translate compile
```

## Set up MySQL

To manage the database server use the mysql command, which should be already installed on your server:

```
$ mysql -u root -p
```

Enter the password you created during the installation of base dependencies above. These commands create a new database called microblog, and a user with the same name that has full access to it:

```sql
mysql> create database microblog character set utf8 collate utf8_bin;
mysql> create user 'microblog'@'localhost' identified by '<db-password>';
mysql> grant all privileges on microblog.* to 'microblog'@'localhost';
mysql> flush privileges;
mysql> quit;
```

If all is well you should now be able to run the migration that creates the tables:

```
(venv) $ flask db upgrade
```

If ever you want to manage your database manually:

```sql
$ mysql -u microblog -p
$ USE microblog;
$ SHOW TABLES;
$ DESCRIBE tablename;
$ exit;
```

## Set up Gunicorn and Supervisor

The supervisor utility uses configuration files that tell it what programs to monitor and how to restart them when necessary. Configuration files must be stored in:

```
$ cd /etc/supervisor/conf.d
$ sudo nano microblog.conf
```

Here is a configuration file called microblog.conf:

```
[program:microblog]
command=/home/jessica/microblog/venv/bin/gunicorn -b localhost:8000 -w 4 microblog:app
directory=/home/jessica/microblog
user=jessica
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```

The command is the only thing that requires a little explanation. The -b option tells gunicorn where to listen for requests. We set this to the internal network interface at port 8000. It's usually a good idea to run Python web applications without external access, and then have a very fast web server that is optimized to serve static files accepting all requests from clients (nginx). This fast web server will serve static files directly, and forward any requests intended for the application to the internal server (gunicorn).

The -w option configures how many workers gunicorn will run. Having four workers allows the application to handle up to four clients concurrently, which for a web application is usually enough to handle a decent amount of clients, since not all of them are constantly requesting content. Depending on the amount of RAM your server has, you may need to adjust the number of workers so that you don't run out of memory.

The microblog:app argument tells gunicorn how to load the application instance. The name before the colon is the module that contains the application, and the name after the colon is the name of the flask application.

After you write this file, reload the supervisor service:

```
$ sudo supervisorctl reload
```

## Set up Nginx

The microblog application server powered by gunicorn is now running privately port 8000. What we need to do now to expose the application to the outside world is to enable the public facing web server on ports 80 and 443.

To be a secure deployment, we'll configure port 80 to forward all traffic to port 443, which is going to be encrypted. We start by creating an SSL certificate. For now it's going to be a *self-signed SSL certificate*, which is okay for testing but not good for a real deployment (because web browsers will warn users that the certificate was not issued by a trusted certificate authority).

```
$ cd ~/microblog
$ mkdir certs
$ openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
  -keyout certs/key.pem -out certs/cert.pem
```

Next, we need to write a configuration file for nginx. In most nginx installations this file needs to be in the /etc/nginx/sites-enabled directory. Nginx installs a test site in this location that we don't really need, so start by removing it:

```
$ sudo rm /etc/nginx/sites-enabled/default
```

Then create a new file:

```
$ sudo nano /etc/nginx/sites-enabled/microblog
```

with the following content:

```
server {
    # listen on port 80 (http)
    listen 80;
    server_name example.com;
    location / {
        # redirect any requests to the same URL but on https
        return 301 https://$host$request_uri;
    }
}
server {
    # listen on port 443 (https)
    listen 443 ssl;
    server_name example.com;

    # location of the self-signed SSL certificate
    ssl_certificate /home/jessica/microblog/certs/cert.pem;
    ssl_certificate_key /home/jessica/microblog/certs/key.pem;

    # write access and error logs to /var/log
    access_log /var/log/microblog_access.log;
    error_log /var/log/microblog_error.log;

    location / {
        # forward application requests to the gunicorn server
        proxy_pass http://localhost:8000;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        # handle static files directly, without forwarding to the application
        alias /home/jessica/microblog/app/static;
        expires 30d;
    }
}
```

This is probably the most intense part in terms of cryptic code. For more information see <https://nginx.org/en/docs/>. After you write this file, tell nginx to reload:

```
$ sudo service nginx reload
```

At this point you should be able to access the app via the ip address. Next, you'll want replace the self-signed certificate with a real one. For this you will first need to purchase a domain name and configure it to point to your server's IP address. Once you have a domain, you can request a free [Let's Encrypt SSL certificate](https://letsencrypt.org/).

Miguel has written a detailed article: [Run your Flask application over HTTPS](https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https).

## Deploying Updates

```
(venv) $ git pull                              # download the new version
(venv) $ sudo supervisorctl stop microblog     # stop the current server
(venv) $ pip install -r requirements.txt       # if you added a library
(venv) $ flask db upgrade                      # upgrade the database
(venv) $ flask translate compile               # upgrade the translations
(venv) $ sudo supervisorctl start microblog    # start a new server
(venv) $ sudo supervisorctl restart microblog  # restart the server
```

## Mapping a Domain to Digital Ocean

1. Updated the nameservers on the domain to digital ocean's (note you can usually do this at the time of purchase):
    ns1.digitalocean.com,  
    ns2.digitalocean.com,  
    ns3.digitalocean.com  

2. Go to the Networking > Domains section of your dashboard and add the domain:
    see this [DNS guide](https://www.digitalocean.com/community/tutorials/an-introduction-to-digitalocean-dns)

3. Set up the A, AAAA Records to map to your droplet.

## SSL Certificates

On visiting the [Let's Encrypt](https://letsencrypt.org/) website, you'll be directed to one of several ACME clients which is software that uses the Acme protocol which typically runs on your web hosts and demonstrates you are the controller of the domain. The recommended one for those with shell access is [Certbot](https://certbot.eff.org/lets-encrypt/ubuntuxenial-nginx):

```
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository universe
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install certbot python-certbot-nginx
$ sudo certbot --nginx
```

After the install you should receive a message:

> Congratulations!  
> Your certificate and chain have been saved at:  
> /etc/letsencrypt/live/zebro.id/fullchain.pem  
> Your key file has been saved at:  
> /etc/letsencrypt/live/zebro.id/privkey.pem  
>
> Your cert will expire on 2018-07-01. To obtain a new or tweaked version of this certificate in the future, simply run certbot again with the "certonly" option. To non-interactively renew *all* of your certificates, run "certbot renew"

So now we need to add these two paths to the nginx config from above. **Note:** As of the certbot version 0.31.0, it automatically puts the new paths in your config. Be sure to check though.

```
$ sudo nano /etc/nginx/sites-enabled/microblog
```

replace the self-signed certificates:

```
# location of the self-signed SSL certificate
ssl_certificate /home/jessica/microblog/certs/cert.pem;
ssl_certificate_key /home/jessica/microblog/certs/key.pem;
```

with the real ones:

```
# location of the SSL certificate
ssl_certificate /etc/letsencrypt/live/zebro.id/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/zebro.id/privkey.pem;
```

After that, stop your app, restart ngnix and start the app up again:

```
$ sudo supervisorctl stop microblog
$ sudo service nginx reload
$ sudo supervisorctl start microblog
```

**Note:** In February 2019, Let's Encrypt ended TLS-SNI-01 type validation. Basically, that meant I needed to reinstall Certbot so that it used the an alternate validation method (HTTP-01, DNS-01, or TLS-ALPN-01). During the update I received the following recommendation:

> IMPORTANT NOTES:
> Your account credentials have been saved in your Certbot
> configuration directory at /etc/letsencrypt. You should make a
> secure backup of this folder now. This configuration directory will
> also contain certificates and private keys obtained by Certbot so
> making regular backups of this folder is ideal.


### Renewing your SSL certificates

At some point you will likely receive an email reminder that your certificate(s) are up for renewal. Also, you can check the expiration date of your certificates through the browser by clicking on the lock icon next to the url. SSH into your server and run the following command from any directory:

```
$ sudo certbot renew
```

Provided everything goes well, you should receive a message like so:

> new certificate deployed with reload of nginx server; fullchain is
>  /etc/letsencrypt/live/review.zebro.id/fullchain.pem
> Congratulations, all renewals succeeded. The following certs have been renewed:
>  /etc/letsencrypt/live/review.zebro.id/fullchain.pem (success)


At this point you should restart your web server:

```
$ sudo supervisorctl restart microblog
```

Note that in order to renew, the `server_name` in your nginx file (`nano /etc/nginx/sites-enabled/microblog`) must match the domain name(s) you entered when setting up certbot. If you have more than one domain name, they should be separated by spaces, not commas. For example:

```
server {
    # listen on port 80 (http)
    listen 80;
    server_name zebro.id microblog.zebro.id;
    location / {
        # redirect any requests to the same URL but on https
        return 301 https://$host$request_uri;
    }
}
server {
    # listen on port 443 (https)
    listen 443 ssl;
    server_name zebro.id microblog.zebro.id;
    ...
```

Miguel has more suggestions to improve the SSL security in his [tutorial](https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https) regarding adding more instructions to the nginx file.

## Redis Server & RQ workers

On a Linux server, adding Redis should be as simple as installing the package from your operating system. For Ubuntu Linux, run:

```
$ sudo apt-get install redis-server.
```

You can start up the server as you normally would in a new ssh session:

```
$ redis-server
```

Or you can start it like this in the same window:

```
$ /etc/init.d/redis-server start
```

Note it can be stopped in the same way:

```
$ /etc/init.d/redis-server stop
```

Test that its running:

```
$ redis-cli ping
```

You need RQ (activate your venv first):

```
(venv) $ pip install rq
```

Now edit the supervisor config file to include an RQ worker:

```
$ sudo nano /etc/supervisor/conf.d/microblog.conf
```

Add this:

```
[program:rq_worker]
; See http://python-rq.org/patterns/supervisor/
command=/home/jessica/microblog/venv/bin/rq worker microblog-tasks
numprocs=1
directory=/home/jessica/microblog
stopsignal=TERM
autostart=true
autorestart=true
```

Reload the supervisor:

```
$ sudo supervisorctl reload
```

To be safe:

```
$ sudo supervisorctl restart microblog
$ sudo supervisorctl start rq_worker
```

Note, this tells you what's running:

```
$ sudo supervisorctl status
```

## Security

- [OWASP top ten](https://www.owasp.org/index.php/OWASP_Top_Ten_Cheat_Sheet)
- [What Are The OWASP Top 10?](https://www.cloudflare.com/learning/security/threats/owasp-top-10/)
- [10 Best Practices to Build Secure Applications](https://blog.sqreen.com/best-practices-build-secure-applications/)

## Misc commands

Should you need to copy a file from your local machine to your server via SSH, note that the path for an Ubuntu user begins with `/home/`, for example:

```
scp /Users/jessicarush/Documents/Coding/Projects/review/data.db review@165.227.39.154:/home/review/backup
```

Check your digital ocean droplet size:

```
$ df / -h
```

Check your digital ocean droplet kernel and system architecture:

```
uname -ir
```

To upgrade your digital ocean droplet kernel and system packages:

```
$ sudo apt-get upgrade
$ sudo apt-get dist-upgrade
```

Shutdown your droplet (for say resizing) with the Ubuntu command:

```
$ sudo shutdown -h now
```

or using the digital ocean command:

```
$ sudo poweroff
```

## Troubleshooting lessons learned

When deploying updates things can break and from my experience the reason is usually pretty straight forward (we forgot to do something) or is weird but easy to fix (an ubuntu specific issue). Often, it's simply getting the right error message that's important.

Ubuntu has a tonne of error logs located in `/var/log/` and so far, in my experience, most of them are cryptic and unhelpful. If having issues reloading or starting your app with:

```
$ sudo supervisorctl restart microblog
$ sudo supervisorctl start microblog
```

The FIRST thing to go is try starting it like you would in your local environment with:

```
$ flask run
```

This way, when it fails, we can see the flask error messages right away. The flask messages tend to be way more useful than the supervisor error logs or the nginx logs.

Some common mistakes I've made and discovered in this way:

- Forgot to pip install a new library that I added to my app
- Used unicode character names e.g. `\N{PARTY POPPER}`. Just don't, some names work on my local env but not on the server. Stick with the hex numbers.
- Forgot to restart the supervisor when making changes to `/etc/supervisor/conf.d/myapp.conf`
- Forgot to restart ssh when making changes to `/etc/ssh/sshd_config`
- Forgot to reload nginx when making changes to `/etc/nginx/sites-enabled/myapp`
- Forgot to `flask db upgrade` the database when columns were added


Summary of the various restart commands:

```
$ sudo reboot
$ sudo service ssh restart
$ sudo service ssh nginx reload
$ sudo supervisorctl reload
$ sudo supervisorctl restart myapp
```
