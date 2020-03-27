# Description

This repository is a small template for easily trying flask with docker-compose.

# Preparation

Please install the following before using this repository.

- docker
- docker-compose

# How to use

Execute app/main.py at startup. Please change as necessary.

## start

```sh
$ docker-compose up -d
```

## teardown

```sh
$ docker-compose down
```

## Example

- get

```sh
$ curl http://localhost/
route get. Hello!
```

- post

```sh
$ curl http://localhost:5001/reply -X POST -H "Content-Type: application/json" -d '{"keyword": "hoge"}'
{
  "Answer": {
    "Text": "route post. keyword is hoge!"
  },
  "Content-Type": "application/json"
}
```
