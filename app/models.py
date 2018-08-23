#!/usr/bin/python3
#coding=utf-8
'''
Created on 2018年8月22日

@author: qcymkxyc
'''
from flask_sqlalchemy import SQLAlchemy
from . import db

class Role(db.Model):
    __tablename__ = "roles"
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64),unique = True)
    users = db.relationship("User",backref = "role",lazy = "dynamic")
    
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))