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
SECRET_KEY = '123456'
USERNAME = 'admin'
PASSWORD = 'admin'

HOST = '127.0.0.1'
PORT = 8000
DEBUG = True

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
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


@app.route('/')
def show_entries():
    cur = g.db.execute('select title ,text from entries order by id desc ')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('login'):
        abort(401)
    g.db.execute('insert into entries(title,text) values (?,?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config.get('USERNAME'):
            error = 'invalid username'
        elif request.form['password'] != app.config.get('PASSWORD'):
            error = 'invalid password'
        else:
            session['login'] = True
            flash('You have logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('login')
    flash('You have logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    init_db()
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
