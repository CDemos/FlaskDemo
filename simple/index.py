#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Flask

app = Flask(__name__)

host = '127.0.0.1'
port = 8000


@app.route('/')
def index():
    return 'welcome'


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
