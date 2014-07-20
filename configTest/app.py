#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Flask


def wrap(fn):
    def wrap_output(*arg, **kwargs):
        print '--start---'
        fn(*arg, **kwargs)
        print '--end--'
        print ''

    return wrap_output


@wrap
def test_from_pyfile():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    print app.config.get('USERNAME')
    print app.config.get('PASSWORD')


@wrap
def test_from_pyfile_in_folder():
    app = Flask(__name__)
    app.config.from_pyfile('conf/config.py')
    print app.config.get('USERNAME')
    print app.config.get('PASSWORD')

@wrap
def test_from_object():
    from ObjConfigs import ProductionConfig,DevelopmentConfig,TestingConfig
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    print app.config.get('URL')
    print ''

    app.config.from_object(DevelopmentConfig)
    print app.config.get('URL')
    print ''

    app.config.from_object(TestingConfig)
    print app.config.get('URL')


if __name__ == '__main__':
    test_from_pyfile()
    test_from_pyfile_in_folder()
    test_from_object()