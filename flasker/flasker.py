#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

import sqlite3
from flask import Flask, request, session, g, redirect
from flask import url_for, abort, render_template, flash
from contextlib import closing


# configuration
# DATABASE = '/tmp/flasker.db'
DATABASE = 'flasker.db'
DEBUG = True
SECRET_KEY = '123456'
USERNAME = 'admin'
PASSWORD = 'admin'

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    # g.db.close()


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


if __name__ == '__main__':
# init_db()
    app.run()