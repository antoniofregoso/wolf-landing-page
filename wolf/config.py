# -*- coding: utf-8 -*-
import os
import configparser

class Config(object):
    config = configparser.ConfigParser() 
    config.read(os.getcwd() +'wolf.ini')
    csrf = config['options']['csrf_secret'] 
    SECRET_KEY = os.environ.get('SECRET_KEY') or csrf
    OPTIONS = config['options']
    SELECTION = []
    for k, v in config['selection'].items():
        SELECTION.append((k, v))