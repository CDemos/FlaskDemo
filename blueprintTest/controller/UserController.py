#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Blueprint, render_template, request,abort
from jinja2 import TemplateNotFound


user_controller = Blueprint('user_controller', __name__, template_folder='controllertemplates', url_prefix='/user')


@user_controller.route('/login', methods=['POST', 'GET'])
def login():
    try :
        return render_template('index.html',title='Index Page')
    except TemplateNotFound as e:
        abort(404)

@user_controller.route('/info/<user_id>')
def user_info(user_id):
    return 'user id is' + user_id