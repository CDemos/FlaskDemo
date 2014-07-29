#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Flask, request, session, make_response,redirect

app = Flask(__name__)

app.secret_key = "12334535671324"
host = '127.0.0.1'
port = 8000


@app.route('/')
def index():
    return 'welcome'


@app.route('/login/<int:id>')
def login(id):
    print(request.cookies)
    resp = make_response("login")
    #10
    resp.set_cookie('name', 'jayin', max_age=10)
    resp.set_cookie('userud', '123456', max_age=30)
    return resp

@app.route('/see')
def see():
    print request.cookies
    print type(request.cookies)
    print help(request.cookies)
    # make_response()
    return "see"

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('name')
    session.clear()
    return resp

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
