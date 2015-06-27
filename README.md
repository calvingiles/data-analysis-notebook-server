data-analysis-notebook-server
============

Portable development environment for data analysis

This defines a Dockerfile and related resources for building an ipython notebook server in a docker container capable of connecting to databases, queues etc. and performing desired analysis.

## Installing
### Simple first time install

* Set up a [docker account](https://www.docker.com/)
* Install [boot2docker](http://boot2docker.io/)
* Init boot2docker:

```bash
$ boot2docker init
$ boot2docker start
$ $(boot2docker shellinit)
$ '$(boot2docker shellinit)' >> ~/.bash_profile
```

### Update your setup to latest

```bash
$ docker pull data-analysis-notebook-server
```

### Starting notebook server

Once the container has been started, navigatge to `http://localhost:443` or, if using boot2docker (i.e. on a mac), get your docker host with `boot2docker ip` and replace `localhost` with that. Login with the password in the `PASSWORD` environment above.

If you want to make this easier, you can add your boot2docker ip to your hosts file with:

```bash
$ sudo echo <your-boot2docker-ip> docker.local >> /etc/hosts
```

then you can navigate to [https://docker.local](https://docker.local)

### More

Go to this [medium blog post](https://medium.com/@calvingiles/snippets-for-troubleshooting-docker-637f510f6a92) for help.
