# Description

This repository is a small template for easily trying flask with docker-compose.

# Preparation

Please install the following before using this repository.

- docker
- docker-compose

# About Docker Environment



# How to use

Execute app/main.py at startup. Please change as necessary.

## start

```sh
$ docker-compose build
$ docker-compose up -d
```

## teardown

```sh
$ docker-compose down
```

## Example

```sh
$ curl https://localhost/hello
Hello world
```
