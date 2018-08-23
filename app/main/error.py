#!/usr/bin/python3
#coding=utf-8
'''
Created on 2018年8月23日

@author: qcymkxyc
'''

from . import main
from flask import render_template

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html",404)

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html",500)