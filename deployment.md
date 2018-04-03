# Deployment

## Traditional Hosting

Traditional hosting, means that the application is installed manually or through a scripted installer on a stock server machine. The process involves installing the application, its dependencies and a production scale web server and configure the system so that it is secure.

## Operating Systems

From a technical point of view, many application can be deployed on any of the major operating systems, a list which includes a large variety of open-source Linux and BSD distributions, and the commercial OS X and Microsoft Windows. Since OS X and Windows are desktop operating systems that are not optimized to work as servers, it makes more sense to choose between a Linux or a BSD operating system. The most popular of the two is Linux. As far as Linux distributions, the most popular is Ubuntu.

## Paid Public Servers

For $5 per month, the following will rent you a virtualized Linux server:

- [Digital Ocean](https://www.digitalocean.com/) (entry level servers have 1GB of RAM)
- [Linode](https://www.linode.com/pricing) (entry level servers have 1GB of RAM)
- [Amazon Lightsail](https://aws.amazon.com/lightsail/) (entry level servers have 512MB of RAM)

## Free Private Server

[Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) are two tools that combined allow you to create a virtual server similar to the paid ones on your own computer. To use these, install both and then create a file name *Vagrantfile* to describe the specs of your virtual machine:

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

For more information see the [vagrant commend line documentation].(https://www.vagrantup.com/docs/cli/)

## SSH

Most of your interactions with the server will be through SSH. On Linux and Mac OS, OpenSSH is already installed. If you are using a third party virtual server, you'll want to make sure to look into adding your ssh keys so you don't have to enter passwords all the time. On Digital Ocean its under settings/security.
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

Since we now have a new user account that can run administrator commands via sudo, there is really no need to expose the root account. To disable root logins, you need to edit the /etc/ssh/sshd_config file on your server. You probably have the vi and nano text editors installed in your server to edit files:
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

At the time of this writing, Digital Ocean's Ubuntu 16.04 comes with Python 3.5. If you want to upgrade try this (untested!):
```
$ sudo add-apt-repository ppa:jonathonf/python-3.6
$ sudo apt-get update
$ sudo apt-get install python3.6
```

Otherwise, consider the following:
```
$ sudo apt-get -y update
$ sudo apt-get -y install python3 python3-venv python3-dev
$ sudo apt-get -y install mysql-server postfix supervisor nginx git
```

- **mysql-server** - MySQL for the database (for postgreSQL, see deployment_digitalocean.md).
- **postfix**  - mail transfer agent, for sending out email.
- **supervisor**  - a tool to monitor the Flask server process. It automatically restarts it if it ever crashes, or if the server is rebooted.
- **ngnix** - the server that accepts all requests that come from the outside world, and forwards them to the application.
- **git** - to download the application directly from its github repo.

Note that the default installation of postfix is likely insufficient for sending email in a production environment. To avoid spam and malicious emails, many servers require the sender server to identify itself through security extensions, which means at the very least you have to have a domain name associated with your server. If you want to learn how to fully configure an email server so that it passes standard security tests, see the following Digital Ocean guides:


- [Postfix Configuration](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-16-04)
- [Adding an SPF Record](https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability)
- [DKIM Installation and Configuration](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-dkim-with-postfix-on-debian-wheezy)

> Postfix is set up with a default configuration. If you need to make
changes, edit */etc/postfix/main.cf* (and others) as needed. After modifying *main.cf*, be sure to run *'/etc/init.d/postfix reload'*.

### Elasticsearch

This service requires a large amount of RAM, so it's only viable if you have a server with more than 2GB of RAM. Note that the Elasticsearch package available in the Ubuntu 16.04 package repository is too old and will not work, you need version 6.x or newer. If you have a big enough server try this tutorial:

[Install and Configure Elasticsearch on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-16-04)

## Use Git to Install the Application from GitHub

You'll need to create a new repo in Github and then push your local repo to it. Once its there you can clone it onto your remote server. First, make sure you're in your home directory:
```
cd ~/
git clone https://github.com/username/reponame.git
```

## Create a Virtual Environment and Install Dependencies

This is done in the same way as you would on your local machine:
```
$ cd <reponame>
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ pip install gunicorn pymysql
```

In addition to the requirements we install the gunicorn package which is a production web server for Python applications and the pymysql package which contains the MySQL driver that enables SQLAlchemy to work with MySQL databases.

## Recreate the .env file

Assuming this file is in the .gitignore, we'll need to create it on the server:
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
mysql -u root -p
```

Enter the password you created during the installation of base dependencies above. These commands create a new database called microblog, and a user with the same name that has full access to it:
```
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

To be a secure deployment, we'll configure port 80 to forward all traffic to port 443, which is going to be encrypted. We start by creating an SSL certificate. For now it's going to ba a *self-signed SSL certificate*, which is okay for testing but not good for a real deployment (because web browsers will warn users that the certificate was not issued by a trusted certificate authority).
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
    server_name _;
    location / {
        # redirect any requests to the same URL but on https
        return 301 https://$host$request_uri;
    }
}
server {
    # listen on port 443 (https)
    listen 443 ssl;
    server_name _;

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


## SSL Certificate

On visiting the [Let's Encrypt](https://letsencrypt.org/) website, you'll be directed to one of several ACME clients which software that uses the Acme protocol which typically runs on your web hosts and demonstrates you are the controller of the domain. The recommended one for those will shell access is [Cerbot](https://certbot.eff.org/lets-encrypt/ubuntuxenial-nginx):

```
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python-certbot-nginx
$ sudo certbot --nginx
```

After the install you should receive a message:
> Your account credentials have been saved in your Certbot configuration directory at /etc/letsencrypt. You should make a secure backup of this folder now. This configuration directory will also contain certificates and private keys obtained by Certbot so making regular backups of this folder is ideal.

And also:

>Congratulations! Your certificate and chain have been saved at:
/etc/letsencrypt/live/zebro.id/fullchain.pem  
Your key file has been saved at:
/etc/letsencrypt/live/zebro.id/privkey.pem  

> Your cert will expire on 2018-07-01. To obtain a new or tweaked version of this certificate in the future, simply run certbot again with the "certonly" option. To non-interactively renew *all* of your certificates, run "certbot renew"

So now we need to add these two paths to the nginx config from above:

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

Miguel has more suggestions to improve the SSL security in his [tutorial](https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https) regarding adding more things to the nginx file.
