#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)

host = '127.0.0.1'
port = 8000

# 使用session 必须设置secret_key
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
    print session.__dict__
    print session
    print "??"
    if 'username' in session:
        return 'Logged in as %s' % session['username']
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    if 'username' in session:
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))
    else:
        return '''
            <p> Not logint yet</p>
            <p> Click</p><a href="./login">Here</a> to login!
        '''


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)

