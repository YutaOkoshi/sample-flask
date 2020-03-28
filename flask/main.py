from flask import Flask, request
import logging
import os

LOG_FILENAME = "{}/config/docker.yaml".format(os.getcwd())
logging.basicConfig(filename=LOG_FILENAME)

app = Flask(__name__)

@app.route('/hello')
def hello():
  hello = "Hello world!!!"
  return hello

@app.route('/')
def index():
  app.logger.info("aaaa")
  return 'hello, {}! this sample app!'.format(request.remote_addr)

if __name__ == "__main__":
  app.run()
