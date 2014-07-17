#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Flask, render_template

app = Flask(__name__)

host = '127.0.0.1'
port = 8000


class User(object):
    def __init__(self, url, username):
        self.url = url
        self.username = username


@app.route('/user')
def user():
    return "User Page"


@app.route('/')
def index():
    web_title = 'Coder'
    title = 'Hello'
    content = 'Flask ,micro web framework for Python'
    show_me = True
    users = [
        User('/user', 'Jayin Ton')
        , User('/user', 'Max Lv')
        , User('/user', 'John Steven')
        , User('/user', 'Cambo Zhang')
    ]
    return render_template('index.html', web_title=web_title, \
                           title=title, content=content, show=show_me, users=users)


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
