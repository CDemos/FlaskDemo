#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Flask, flash, redirect, render_template, request, url_for



host = '127.0.0.1'
port = 8000

username = "admin"
password = "admin"

app = Flask(__name__)
app.secret_key = "asdf1234"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #最好要检查request.form['username'] 是否为空
        if request.form['username'] != username or request.form['password'] != password:
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
