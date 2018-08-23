#!/usr/bin/python3
#coding=utf-8
'''
Created on 2018年8月22日

@author: qcymkxyc
'''
import os

username = "root"
pw = "123456"
host = "47.94.80.98"
database = "test"

basedir  = os.path.dirname(__name__)

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = "Flasky Admin <flasky@example.com>"
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True    
    
    
    @staticmethod
    def init_app(app):
        pass
    

class DevelopementConfig(Config):
    
    DEBUG = True
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    
#     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}/{3}".format(username,pw,host,database)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@47.94.80.98/test"
#     SQLALCHEMY_DATABASE_URL = os.environ.get("DEV_DATABASE_URL") or "mysql+pymysql://" + os.path.join(basedir,"data-dev.mysql")
    
class TestingConfig(Config):
    TESTING = True
    
    
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}/{3}".format(username,pw,host,database)
#     SQLALCHEMY_DATABASE_URL = os.environ.get("DEV_DATABASE_URL") or "mysql+pymsql://" + os.path.join(basedir,"data-test.mysql")
    
class ProductConfig(Config):

    
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{0}:{1}@{2}/{3}".format(username,pw,host,database)    
#     SQLALCHEMY_DATABASE_URL = os.environ.get("DEV_DATABASE_URL") or "mysql+pymysql://" + os.path.join(basedir,"data.mysql")
    
config = {
    "development" : DevelopementConfig,
    "testing" : TestingConfig,
    "production" : ProductConfig,
    
    "default" : DevelopementConfig
    }