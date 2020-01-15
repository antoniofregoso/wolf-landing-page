import os
import configparser

class Config(object):
    config = configparser.ConfigParser()
    config.read('wolf.ini')
    csrf = config['options']['csrf_secret']
    SECRET_KEY = os.environ.get('SECRET_KEY') or csrf