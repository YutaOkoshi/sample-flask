# Description

This repository is a small template for easily trying flask with docker-compose.

# Preparation

Please install the following before using this repository.

- docker
- docker-compose

# About Docker Environment

![aboudt image](https://user-images.githubusercontent.com/37532269/77821850-b1962f00-7130-11ea-8596-759a19bf9b61.png)

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
