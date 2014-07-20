#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Blueprint, render_template, request


user_controller = Blueprint('user_controller', __name__, template_folder='mytemplates', url_prefix='/user')


@user_controller.route('/login', methods=['POST', 'GET'])
def login():
    return 'login page'


@user_controller.route('/info/<user_id>')
def user_info(user_id):
    return 'user id is' + user_id