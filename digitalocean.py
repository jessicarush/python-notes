'''Deploying Flask Apps to DigitalOcean'''

# In digitalocean, servers are called 'droplets'. To create a new server,
# find the 'create new droplet' button.

# Choose an image (this is the operating system that we'll run)
# - choose Ubuntu 16.04 x64  This is an 'LTS' (longterm support) distribution.

# Choose a size
# Add block storage: leave blank
# Choose a datacenter region: choose closest to your users for speed.
# Additional options:
# - private networking: allows droplets to communicate with each other
#   without going through the internet.
# - backups: adds weekly backups for extra $
# - IPv6: be default droplets run on IPv4
# - User data: fancy cloud init feature
# - monitoring: adds a droplet with metrics and monitoring features
# Add your SSH keys: optional of course
# Finalize and create: choose how many droplets and hostname

# If you added an ssh key you'll connect to the server via your own terminal:

# ssh root@the.droplets.ip.address

# If you didn't add and ssh, you'll get emailed a big, long, nasty password.
# From the droplets dashboard, choose to 'Access Console' and you'll need to
# enter the username (root), that long, nasty password (twice), then your new
# password (twice).

# The first commend you'll want to run is:

# apt-get update

# this tells apt (Ubuntu's pip) to check if there's anything already installed
# on the server that can be updated.


# -----------------------------------------------------------------------------
# Creating a new user
# -----------------------------------------------------------------------------
# It's a good idea to create a new user on your server so your not always
# using root. Root is a super user and should only be used when necessary.

# root@malaspina:~# adduser jessica

# This creates a new user and a new 'group'.

# add sudo privileges to the new user:

# root@malaspina:~# usermod -aG sudo jessica

# set up ssh public key authentication for your new user:

# manually copy your public key (cat ~/.ssh/id_rsa.pub)

# back on the droplet server, switch to the new user:

# root@malaspina:~# su - jessica

# In the users home directory, create .ssh with the correct permissions:

# $ mkdir ~/.ssh
# $ chmod 700 ~/.ssh

# create and open a the authorized_keys file:

# $ nano ~/.ssh/authorized_keys

# paste in your public key, hit ctrl-x to exit, y to save the changes and
# enter to confirm the name.

# restrict the permissions of the authorized_keys file:

# $ chmod 600 ~/.ssh/authorized_keys

# Double check some config settings:

# sudo nano /etc/ssh/sshd_config

# Make sure the following commands are set like this:
# PasswordAuthentication no
# PubkeyAuthentication yes
# ChallengeResponseAuthentication no

# PermitRootLogin no **optional**

# If you had to make changes here, be sure to CTRL-X, Y, ENTER, then:

# sudo systemctl reload sshd

# These instructions came from:
# https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04


# -----------------------------------------------------------------------------
# Installing postgresql
# -----------------------------------------------------------------------------
# apt-get install postgresql postgresql-contrib

# When you do this you'll see the following near the end of the installation:
# Creating new cluster 9.5/main ...
#   config /etc/postgresql/9.5/main
#   data   /var/lib/postgresql/9.5/main
#   locale en_US.UTF-8
#   socket /var/run/postgresql
#   port   5432

# Note that when we install postgresql, it also creates a new user on our
# digitalocean server. This new user is the owner of the postgresql
# installation. You'll want to switch over to that user:

# root@malaspina:~# sudo -i -u postgres

# The command line prompt should reflect this switch:

# postgres@malaspina:~$

# Now, to connect to the database type: psql

# Note, the database will have the same name as the user: postgres
# You can check that by typing: \conninfo

# If we wanted, we good now run sql commands here.

# To exit from the database, type: \q

# To logout of the postgres user and return to root type: exit


# -----------------------------------------------------------------------------
# Creating and linking a new user to postgresql
# -----------------------------------------------------------------------------
# First ssh to the server as the user, then sudo switch to the postgres user:

# ssh jessica@your.ip.add.here
# sudo -i -u postgres

# For some reason, we now have to create a new postgres user and password:

# createuser jessica -P

# Create a new database for that user. By default when typing psql it will
# connect to a database that is the same name as the user. I don't know if
# this is a rule yet.

# create db jessica

# if you want to delete a database you can type the command 'dropdb'

# now 'exit' from the postgres user and try connecting to the users database by
# typing 'psql'. To double check type '\conninfo' and '\q' to quit.

# Note: postrges won't ask for a password when the db name is the same as the
# username which makes sense to me but if, for some reason, you  want to force
# it to ask for a password every time, then try this:

# $ sudo vi /etc/postgresql/9.5/main/pg_hba.conf

# scroll down to the following lines:

# local   all             postgres                         peer
# TYPE    DATABASE        USER            ADDRESS          METHOD
# "local" is for Unix domain socket connections only
# local   all             all                              peer
# IPv4 local connections:
# host    all             all             127.0.0.1/32     md5
# IPv6 local connections:
# host    all             all             ::1/128          md5

# Note the column names type, database user address method. The first line
# says if we are connecting locally we have access to all databases as the
# postgres user. Peer "obtain the client's operating system user name from
# the operating system and check if it matches the requested database user
# name. This method is only available for local connections".

# The next line says the same thing but for all users. All users have all
# access just like the postgres user.

# The third and fourth lines say if users are connecting though the internet,
# all users can have access to all databases but the md5 method says a password
# is required. Therefor, if you want to, you could change all local users to
# md5 as well. If you make changes here remember 'i' to insert and ':wq' to
# write and quit.

# NOTE: apparently SQALchemy requires you to have a password protected
# connection to your database. For this reason, make the changes above.

# https://www.postgresql.org/docs/current/static/auth-pg-hba-conf.html


# -----------------------------------------------------------------------------
# Installing nginx and enabling a Firewall
# -----------------------------------------------------------------------------
# NGINX is a free, open-source, HTTP server and reverse proxy, as well as an
# IMAP/POP3 proxy server. In layman's terms, it can act at a gateway between
# our app and external users. It will accept and direct incoming requests.
# We can configure it so that the request goes straight to our app. The reason
# we would want to use ngnix to do this is:
# - it communicates well with uwsgi
# - enables multi-threaded operations in our flask app
# - also allows you to run multiple flask apps simultaneously on your server.
# - it can direct incoming requests to different apps based on some parameters.

# Assuming you're logged into your server:

# $ sudo apt-get update
# $ sudo apt-get install nginx

# We need to enable the firewall and allow nginx and ssh access:

# $ sudo ufw status
# $ sudo ufw allow 'Nginx HTTP'
# $ sudo ufw allow ssh
# $ sudo ufw allow https
# $ sudo ufw enable

# If you check 'sudo ufw status' again, you should see both Ngnix ans ssh are
# allowed access. Note ssh is indicated as '22'. 22 is the port number that
# ssh uses. You could also allow ssh by saying 'sudo ufw allow 22'. Therefor,
# if you've configured your ssh daemon to use another port, just type that
# port number instead. FYI you can also allow ranges of ports and IP addresses.
# see here for more info:

# https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-16-04

# Check that nginx is running with the system controller:

# $ systemctl status nginx

# FYI you can also start and stop services like ngnix this way:

# $ systemctl start nginx
# $ systemctl stop nginx
# $ systemctl restart nginx


# -----------------------------------------------------------------------------
# Configure nginx
# -----------------------------------------------------------------------------
# At some point you'll need to configure nginx to work with (access) our app:

# $ sudo vi /etc/nginx/sites-available/items-rest.conf

# Insert the following (without '''):

'''
server {
listen 80;
real_ip_header X-Forwarded-For;
set_real_ip_from 127.0.0.1;
server_name localhost;

location / {
include uwsgi_params;
uwsgi_pass unix:/var/www/html/items-rest/socket.sock;
uwsgi_modifier1 30;
}

error_page 404 /404.html;
location = /404.html {
root /usr/share/nginx/html;
}

error_page 500 502 503 504 /50x.html;
location = /50x.html {
root /usr/share/nginx/html;
}
}
'''
# esc, :wq

# listen 80;
# - default http port, because its the default we don't need to
#   include it in our users get requests. Normally somewhere in the
#   request string we'd need to have :5432 if that was our port.

# real_ip_header X-Forwarded-For;
# - forwards the IP address of the requester to our flask app.

# set_real_ip_from 127.0.0.1;
# - after it forwards the IP address, it sets it to the local IP address

# location / {
# - whenever someone accesses the root location / of the server, they'll
#   get redirected somewhere (our flask app).

# include uwsgi_params;
# - allows it to communicate with uwsgi which we're using in part because it
#   allows our program to run multiple threads more efficiently and to restart
#   threads if they fail. uwsgi is pretty complicated but these two apparently
#   work well together.

# uwsgi_pass unix:/var/www/html/items-rest/socket.sock;
# - the connection point between our flask app and ngnix.
#   socket.sock is a file we'll need to create shortly.

# uwsgi_modifier1 30;
# - tell threads when to die if they become blocked

# error_page 404 /404.html;
# - if there is a 404 error, the user will be redirected to this page

# location = /404.html {
# root /usr/share/nginx/html;
# - serve the 404.html file from this directory

# Once you've made these changes to the items-rest.conf file, you'll also
# need to enable it. The following creates a soft link between the config
# file and the sites-enabled directory.

# $ sudo ln -s /etc/nginx/sites-available/items-rest.conf /etc/nginx/sites-enabled/

# Apparently we need to remove an nginx default. This doesn't actually
# remove the file, it's just a link file, the actual file still sits in the
# 'sites-available' folder:

# $ sudo rm /etc/nginx/sites-enabled/default
# $ sudo systemctl reload nginx
# $ sudo systemctl restart nginx

# Note, reload will reload the configuration for nginx
# restart does just that.


# -----------------------------------------------------------------------------
# Create directories, git clone your app, install python
# -----------------------------------------------------------------------------
# Create the directory where the application files will be placed, give
# access to the user, and then cd into that directory. This is the same path we
# wrote in the config file:

# $ sudo mkdir /var/www/html/items-rest
# $ sudo chown jessica:jessica /var/www/html/items-rest
# $ cd /var/www/html/items-rest/

# Clone our python app from github. Be sure to put a space followed by a period
# after the url to indicate we want to clone into the current directory:

# $ git clone https://github.com/jessicarush/testing.git .

# Make a log directory (note we don't ned to use sudo now because of chown):

# $ mkdir log

# Install packages required for python and psycopg2:

# $ sudo apt-get install python-pip python3-dev libpq-dev

# Create a virtual environment for the app:

# $ sudo apt-get install python3-venv
# $ python3 -m venv venv
# $ source venv/bin/activate

# $ pip install --upgrade pip
# $ pip install wheel
# $ pip install -r requirements.txt


# -----------------------------------------------------------------------------
# Set up ubuntu 'service', uwsgi.ini
# -----------------------------------------------------------------------------
# $ cd /var/www/html/items-rest
# So at this point in the above directory we should see our app, Procfile,
# requirements.txt, runtime.txt, uwsgi.ini, venv, and log directory.

# Next we'll create an ubuntu "service". A service is a daemon that you can
# tell ubuntu to run when the server starts or restart if you need to apply an
# updated config file, etc. The service then runs something else (like our
# uwsgi). A service also lets you do things like set environment variables.

# $ sudo vi /etc/systemd/system/uwsgi_items_rest.service

# Insert the following (without ''')

'''
[Unit]
Description=my uWSGI items rest

[Service]
Environment=DATABASE_URL=postgres://jessica:cinnamon-sticks@localhost:5432/jessica
ExecStart=/var/www/html/items-rest/venv/bin/uwsgi --master --emperor /var/www/html/items-rest/uwsgi.ini --die-on-term --uid jessica --gid jessica --logto /var/www/html/items-rest/log/emperor.log
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
'''
# esc, :wq

# Note in the environment variable above, the last 'jessica' is the name of the
# database.

# Now we have to edit the following file:

# $ cd /var/www/html/items-rest
# $ vi uwsgi.ini

# If coming from heroku, the file should look like this (see heroku.py):
'''
[uwsgi]
http-socket = :$(PORT)
master = true
die-on-term = true
module = app:app
memory-report = true
'''
# Delete all that (d-shift-G), i to insert and enter:
'''
[uwsgi]
base = /var/www/html/items-rest
; our run.py file
app = run
module = %(app)
home = %(base)/venv
pythonpath = %(base)
socket = %(base)/socket.sock
chmod-socket = 777
; change these if you want but there may be limits on the droplet
processes = 4
threads = 4
; number of seconds before killing if a process/thread is stuck
harakiri = 15
; app refers to the variable name in our app.py file
callable = app
logto = /var/www/html/items-rest/log/%n.log
'''
# esc, :wq

# Note in the above %n is a uwsgi magic variable for the filename. See:
# http://uwsgi-docs.readthedocs.io/en/latest/Configuration.html

# Now we should be able to start our flask app by starting the service:

# $ sudo systemctl start uwsgi_items_rest

# You won't really be able to tell if it's running but if you open the log:

# $ vi log/uwsgi.log

# You should see some information. As well, test the requests via postman,
# then check back at the log.


# -----------------------------------------------------------------------------
# updating your api
# -----------------------------------------------------------------------------
# If you've made changes to your app, you'll need to commit to git,
# push to github, then on the server do a git pull then restart the
# uwsgi_items_rest process:

# local machine:
# $ git add -A
# $ git commit -m 'Description of changes'
# $ git push -u origin master

# server:
# $ cd /var/www/html/items-rest/
# $ git pull
# $ sudo systemctl start uwsgi_items_rest


# -----------------------------------------------------------------------------
# Attaching a domain name to your digitalocean server:
# -----------------------------------------------------------------------------

# Once you've bought a domain, you can use a service like cloudflare to
# set up the DNS to connect to your servers ip. Cloudflare is a "content
# delivery network". Essentially it can be used to sit in front of our server.
# You can do various things like store the site on their server to increase
# speed (I think they do this through caching so beware). They've got security
# features and things that prevent "denial of service attacks". You can set up
# SSL certificates through them as well.

# The main thing is you need to change the nameservers from wherever you
# bought the site to wherever your actual site lives. If you were using
# cloudflare as an in between.

# If you were going straight to digitalocean you'd change the nameservers to:
# ns1.digitalocean.com
# ns2.digitalocean.com

# From there you can go to digitalocean's dashboard and choose Networking >
# Domains. Follow the steps here:
# https://www.digitalocean.com/community/tutorials/how-to-set-up-a-host-name-with-digitalocean

# Basically what you end up doing is editing your domains DNS records
# (A, AAAA, CNAME, MX, TXT).

# https://school-of-code.gitbooks.io/rest-apis-with-flask-and-python/content/domains-and-https/modifying-our-dns-records.html


# -----------------------------------------------------------------------------
# Setting up an SSL certificate (https://)
# -----------------------------------------------------------------------------
# This is a three step process. First you need to get a certificate and a key.
# Then you need to copy those keys as files into your server directory. Lastly,
# you need to modify the ngnix config file.

# 1. Getting the certificate & key:
#    This will be different depending on what "certificate authority" you're
#    using. If cloudflare, you'd go to the 'crypto' tab. Then there a spot to
#    enable SSL then lower down the page, create a certificate. When you create
#    a certificate, it will give you two strings... an 'origin certificate' and
#    a 'private key'. There may be an option for format, just use PEM (default).

# 2. Copying the certifiacte/key to your server:
#    $ ssh jessica@159.203.42.120
#    $ sudo mkdir /var/www/ssl
#    $ sudo touch var/www/ssl/mydomain.com.pem
#    $ sudo touch var/www/ssl/mydomain.com.key
#    $ sudo vi var/www/ssl/mydomain.com.pem   (paste in the origin certificate)
#    $ sudo vi var/www/ssl/mydomain.com.key   (paste in the private key)

# 3. Modify the ngnix config file:
#    $ sudo vi /etc/nginx/sites-enabled/items-rest.conf

# before:
'''
server {
listen 80;
real_ip_header X-Forwarded-For;
set_real_ip_from 127.0.0.1;
server_name localhost;
{more}
'''

# after:
'''
server {
listen 443 default_server;
server_name mydomain.com;
ssl on;
ssl_certificate      var/www/ssl/mydomain.com.pem;
ssl_certificate_key  var/www/ssl/mydomain.com.key;
real_ip_header X-Forwarded-For;
set_real_ip_from 127.0.0.1;
{more}
'''

# $ sudo systemctl reload nginx
# $ sudo systemctl restart nginx

# You can leave it at that, but note that your site will only work on https://
# and not on http://. If you want http as well, look into a redirect through
# cloudflare or wherever.

# https://www.digitalocean.com/community/tutorials/how-to-install-an-ssl-certificate-from-a-commercial-certificate-authority


# -----------------------------------------------------------------------------
# Troubleshooting
# -----------------------------------------------------------------------------

# If you get locked out of ssh, try using the console. See here to set up
# a password for the console:
# https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-console-to-access-your-droplet

# If you rebuild your droplet and you get a weird warning when you try to ssh
# again (WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!), delete the old
# info in your known hosts file by typing:

# $ ssh-keygen -R [your.ip.address.here]

# If you've made changes to your nginx config, don't forget to reload & restart,
# as wall as restart your app:

# $ sudo systemctl reload nginx
# $ sudo systemctl restart nginx
# $ sudo systemctl restart uwsgi_items_rest
