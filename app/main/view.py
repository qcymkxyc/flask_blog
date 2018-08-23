#!/usr/bin/python3
#coding=utf-8
'''
Created on 2018年8月23日

@author: qcymkxyc
'''
from flask import render_template
from flask import session,redirect,url_for

from . import main
# from .. import bootstrap
# from .. import db
from .form import NameForm

@main.route("/",methods = ["GET","POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session["name"] = form.name.data
        return redirect(url_for(".index"))
    return render_template("index.html",form = form,name = session.get("name"))

