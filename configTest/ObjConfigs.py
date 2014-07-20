#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    URL = ''


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    URL = 'http://foo.com/api/product/'


class DevelopmentConfig(Config):
    DEBUG = True
    URL = 'http://foo.com/api/dev/'


class TestingConfig(Config):
    TESTING = True
    URL = 'http://foo.com/api/test/'