#!/usr/bin/python3
#coding=utf-8
'''
Created on 2018年8月23日

@author: qcymkxyc
'''

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField("What is your name?",[Required()])
    submit = SubmitField("Submit")
        