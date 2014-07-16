#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Flask, request


host = '127.0.0.1'
port = 8000

app = Flask(__name__)


@app.before_request
def before_request():
    print("before_request")
    print request


# 必须返回response
@app.after_request
def after_request(res):
    print "after_request"
    print res
    return res


@app.route('/requesting', methods=['GET'])
def requesting():
    print "requesting!"
    return "requesting"


@app.route('/', methods=['GET'])
def index():
    return "Welcome"


@app.route('/post', methods=['POST'])
def add():
    return "Post!"


@app.route('/put', methods=['PUT'])
def put():
    return "PUT"


@app.route('/delete', methods=['DELETE'])
def delete():
    return "DELETE"


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)










