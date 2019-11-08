# Deployment using Docker Containers


Containers are built on a lightweight virtualization technology that allows an application, along with its dependencies and configuration to run in complete isolation, but without the need to use a full blown virtualization solution such as virtual machines, which need a lot more resources and can sometimes have a significant performance degradation in comparison to the host. A system configured as a container host can execute many containers, all of them sharing the host's kernel and direct access to the host's hardware. This is in contrast to virtual machines, which have to emulate a complete system, including CPU, disk, other hardware, kernel, etc. A container has its own file system, and can be based on an operating system that is different than the one used by the container host.

## Table of contents

<!-- toc -->

- [Install Docker](#install-docker)
- [Build a Container Image](#build-a-container-image)
- [Starting a Container](#starting-a-container)
- [Using Third-Party "Containerized" Services](#using-third-party-containerized-services)
- [Adding a MySQL Container](#adding-a-mysql-container)
- [Adding an Elasticsearch Container](#adding-an-elasticsearch-container)
- [Redis server and RQ workers](#redis-server-and-rq-workers)
- [The Docker Container Registry](#the-docker-container-registry)
- [Deployment of Containerized Applications](#deployment-of-containerized-applications)

<!-- tocstop -->

## Install Docker

There are two editions of Docker, a [free community edition (CE)](https://www.docker.com/community-edition) and a subscription based enterprise edition (EE). Once Installed you can check that its running by typing:
```
$ docker version
```

## Build a Container Image

A container image is a template that is used to create a container. It contains a complete representation of the container file system, along with various settings pertaining to networking, start up options, etc.

A good approach is to generate the container image through a script. The command that creates scripted container images is `docker build`. This command reads and executes build instructions from a file called Dockerfile. Each line in the Dockerfile is a command.

Dockerfile:
```
FROM python:3.6-alpine

RUN adduser -D microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
```

The `FROM` command specifies the base container image on which the new image will be built. The idea is that you start from an existing image, add or change some things, and end up with a derived image. Images are referenced by a name and a tag, separated by a colon. The name of our chosen image is python, which is the official Docker image for Python. The tags for this image allow you to specify the interpreter version and base operating system. The 3.6-alpine tag selects a Python 3.6 interpreter installed on Alpine Linux. The Alpine Linux distribution is often used instead of more popular ones such as Ubuntu because of its small size. You can [see what tags are available for Python here](https://hub.docker.com/r/library/python/tags/).

The `WORKDIR` command sets a default directory where the application is going to be installed. The new default directory is going to apply to any remaining commands in the Dockerfile, and also later when the container is executed.

The `RUN chmod` command ensures that the new boot.sh file (contents below) is correctly set as an executable file. If you are working on Mac OS X or Linux you probably don't need this statement, but it does not hurt to have it anyway.

The `RUN chown` command that follows sets the owner of all the directories and files that were stored in /home/microblog as the new microblog user. Even though I created this user near the top of the Dockerfile, the default user for all the commands remained root, so all these files need to be switched to the microblog user so that this user can work with them when the container is started.

The `USER` command in the next line makes this new microblog user the default for any subsequent instructions, and also for when the container is started.

The `EXPOSE` command configures the port that this container will be using for its server.

Finally, the `ENTRYPOINT` command defines the default command that should be executed when the container is started. This is the command that will start the application web server.

boot.sh:
```
#!/bin/sh
source venv/bin/activate
flask db upgrade
flask translate compile
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app
```

`exec` triggers the process running the script to be replaced with the command given, instead of starting it as a new process. This is important, because Docker associates the life of the container to the first process that runs on it. In cases like this one, where the start up process is not the main process of the container, you need to make sure that the main process takes the place of that first process to ensure that the container is not terminated early by Docker.

In Docker, anything that the container writes to stdout or stderr will be captured and stored as logs for the container. For that reason, the `--access-logfile` and `--error-logfile` are both configured with a `-`, which sends the log to standard output so that they are stored as logs by Docker.

With the Dockerfile created, you can now build a container image:
```
$ docker build -t microblog:latest .
```

The `-t` argument sets the name and tag for the new container image. The `.` indicates the base directory where the container is to be built. This is the directory where the Dockerfile is located. The build process is going to evaluate all the commands in the Dockerfile and create the image, which will be stored on your own machine.

You can obtain a list of the images that you have locally with the docker images command:
```
$ docker images
```

Any time you make changes to the application, you can update the container image by running the build command again.


## Starting a Container

With an image created, you can now run the container version of the application. This is done with the `docker run` command, which usually takes a large number of arguments. Here's a basic example:

```
$ docker run --name microblog -d -p 8000:5000 --rm microblog:latest
```
The `--name` option provides a name for the new container. The `-d` option tells Docker to run the container in the background. Without `-d` the container runs as a foreground application, blocking your command prompt. The `-p` option maps container ports to host ports. The first port is the port on the host computer, and the one on the right is the port inside the container. The above example exposes port 5000 in the container on port 8000 in the host, so you will access the application on 8000, even though internally the container is using 5000. The `--rm` option will delete the container once it is terminated. While this isn't required, containers that finish or are interrupted are usually not needed anymore, so they can be automatically deleted. The last argument is the container image name and tag to use for the container.

In addition to these, you also use the run command to set all your environmental variables. That's how the run command becomes extremely long:
```
$ docker run --name microblog -d -p 8000:5000 --rm \
    -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com \
    -e MAIL_PORT=587 \
    -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=<gmail-username> \
    -e MAIL_PASSWORD=<gmail-password> \
    microblog:latest
```

After you run the above command, you can access the application at <http://localhost:8000>.

The output of docker run is the ID assigned to the new container. This is a long hexadecimal string, that you can use whenever you need to refer to the container in subsequent commands. In fact, only the first few characters are necessary, enough to make the ID unique.

If you want to see what containers are running, you can use the docker ps command:
```
$ docker ps
```

If you now want to stop the container, you can use docker stop with the short ID number from the `docker ps` command:
```
$ docker stop 021da2e1e0d3
```

If you want to view logs and any Python stack traces:
```
$ docker logs microblog
```

## Using Third-Party "Containerized" Services

The file system in a container is ephemeral, meaning that it goes away when the container goes away. You can write data to the file system, and the data is going to be there if the container needs to read it, but if for any reason you need to recycle your container and replace it with a new one, any data that the application saved to disk is going to be lost forever.

A good design strategy for a container application is to make the application containers stateless. If you have a container that has application code and no data, you can throw it away and replace it with a new one without any problems, the container becomes truly disposable, which is great in terms of simplifying the deployment of upgrades.

But of course, this means that the data must be put somewhere outside of the application container. The Docker Container Registry contains images for many other languages, databases and other services. The effort to install third party services is reduced to finding an appropriate image in the registry, and starting it with a docker run command with proper arguments.

What we can do is create additional containers, say one for a MySQL database, and another one for the Elasticsearch service, and then access these two new containers through the `run` command.

## Adding a MySQL Container

MySQL has public container images available on the Docker registry. Like your own app container, MySQL relies on environment variables that need to be passed to docker run. There are many MySQL images in the registry, you can find detailed information about one that is [officially maintained by the MySQL team here](https://hub.docker.com/r/mysql/mysql-server/).

The docker run command that starts a MySQL server:
```
$ docker run --name mysql -d \
    -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=microblog \
    -e MYSQL_USER=microblog \
    -e MYSQL_PASSWORD=<db-password> \
    mysql/mysql-server:5.7
```

On any machine that you have Docker installed, you can run the above command and you'll get a fully installed MySQL server with a randomly generated root password, a brand new database called microblog, and a user with the same name that is configured with full permissions to access the database.

On the application side, add a MySQL client package to the Dockerfile:
```
# ...
RUN venv/bin/pip install gunicorn pymysql
# ...
```

Remember, anytime you change something, you need to rebuild the container image:
```
$ docker build -t microblog:latest .
```

Now we can start the app again with a link to the database container:
```
$ docker run --name microblog -d -p 8000:5000 --rm \
    -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com \
    -e MAIL_PORT=587 \
    -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=<your-gmail-username> \
    -e MAIL_PASSWORD=<your-gmail-password> \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://microblog:<db-password>@dbserver/microblog \
    microblog:latest
```
The `--link` option tells Docker to make another container accessible to this one. The argument contains two names separated by a colon. The first part is the name or ID of the container to link that we created above. The second part defines a hostname that can be used in this container to refer to the linked one. Here we used dbserver as generic name that represents the database server.

Sometimes it takes a few seconds for the MySQL container to get up and running. In order to avoid possible fails when the *boot.sh* script tries to run flask db migrate add this:

boot.sh:
```
#!/bin/sh
source venv/bin/activate
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done
flask translate compile
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app
```

## Adding an Elasticsearch Container

The [Elasticsearch documentation for Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html) shows how to run the service as a *single-node* for development, and as a *two-node* production-ready deployment. This example just uses single-node:

The container is started with the following command:
```
$ docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 --rm \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch-oss:6.1.1
```

The Elasticsearch image that I'm using follows the pattern <registry>/<account>/<name>:<tag>, which includes the address of the registry as the first component. This syntax is used for images that are not hosted in the Docker registry. In this case Elasticsearch runs their own container registry service at docker.elastic.co instead of using the main registry maintained by Docker.

We can modify the start command to create a link to it and set the Elasticsearch service URL:
```
$ docker run --name microblog -d -p 8000:5000 --rm \
    -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com \
    -e MAIL_PORT=587 \
    -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=<your-gmail-username> \
    -e MAIL_PASSWORD=<your-gmail-password> \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://microblog:<db-password>@dbserver/microblog \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    microblog:latest
```

## Redis server and RQ workers

To add a Redis server, you first need to create a Redis container. For this you can use one of the official Redis images from the Docker registry:
```
$ docker run --name redis -d -p 6379:6379 redis:3-alpine
```

When you run your application you will need to link the redis container and set the REDIS_URL environment variable, similar to how a MySQL container is linked. Here is a complete command to start the application including a redis link:
```
$ docker run --name microblog -d -p 8000:5000 --rm \
    -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com \
    -e MAIL_PORT=587 \
    -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=<your-gmail-username> \
    -e MAIL_PASSWORD=<your-gmail-password> \
    --link mysql:dbserver \
    --link redis:redis-server \
    -e DATABASE_URL=mysql+pymysql://microblog:<db-password>@dbserver/microblog \
    -e REDIS_URL=redis://redis-server:6379/0 \
    microblog:latest
```

Finally, you will need to run one or more containers for the RQ workers. Because the workers are based on the same code as the main application, you can use the same container image you use for your application, overriding the start up command so that the worker is started instead of the web application. Here is an example docker run command that starts a worker:
```
$ docker run --name rq-worker -d --rm \
    -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com \
    -e MAIL_PORT=587 \
    -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=<your-gmail-username> \
    -e MAIL_PASSWORD=<your-gmail-password> \
    --link mysql:dbserver \
    --link redis:redis-server \
    -e DATABASE_URL=mysql+pymysql://microblog:<db-password>@dbserver/microblog \
    -e REDIS_URL=redis://redis-server:6379/0 \
    --entrypoint venv/bin/rq \
    microblog:latest worker -u redis://redis-server:6379/0 microblog-tasks
```

Overriding the default start up command of a Docker image is a bit tricky because the command needs to be given in two parts. The --entrypoint argument takes just the executable name, but the arguments (if any) need to be given after the image and tag, at the end of the command line. Note that rq needs to be given as venv/bin/rq so that it works without having the virtual environment activated.

## The Docker Container Registry

You can make your own container images available to others, by pushing them to the Docker registry. To do this you'll need a Docker account then:
```
$ docker login
$ docker tag microblog:latest <your-docker-registry-account>/microblog:latest
$ docker push <your-docker-registry-account>/microblog:latest
```
<https://hub.docker.com/>

## Deployment of Containerized Applications

One of the best things about having your application running in Docker containers is that once you have the containers tested locally, you can take them to any platform that offers Docker support. For example, Digital Ocean, Linode or Amazon Lightsail.
