#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

import os
from FlaskDemo.flasker import flasker
import unittest
import tempfile


class FlaskerTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flasker.app.config['DATABASE'] = tempfile.mkstemp()
        flasker.app.config['TESTING'] = True
        self.app = flasker.app.test_client()
        flasker.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flasker.app.config['DATABASE'])

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def test_login_logout(self):
        rv = self.login(flasker.app.config['USERNAME'], flasker.app.config['PASSWORD'])
        assert 'You have logged in' in rv.data

        rv = self.logout()
        assert 'You have logged out' in rv.data

        rv = self.login('adminx', 'default')
        assert 'invalid username' in rv.data

        rv = self.login('admin', 'defaultx')
        assert 'invalid password' in rv.data

    def test_messages(self):
        self.login(flasker.app.config['USERNAME'], flasker.app.config['PASSWORD'])
        rv = self.app.post('/add', data=dict(
            title='Test',
            text='this is content'
        ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert 'Test' in rv.data
        assert 'this is content' in rv.data


if __name__ == '__main__':
    unittest.main()
