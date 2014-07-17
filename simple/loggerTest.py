#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Flask

app = Flask(__name__)

host = '127.0.0.1'
port = 8000


@app.route('/')
def index():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return 'welcome'


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
