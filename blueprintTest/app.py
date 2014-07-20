#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

# todo :测试template~

from flask import Flask
from controller.UserController import user_controller

app = Flask(__name__)

host = '127.0.0.1'
port = 8000

app.register_blueprint(user_controller)


@app.route('/')
def index():
    return 'welcome'


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
