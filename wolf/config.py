# -*- coding: utf-8 -*-
import os
import configparser
import xmlrpc.client

class Config(object):
    config = configparser.ConfigParser() 
    config.read('wolf.ini')
    csrf = config['options']['csrf_secret'] 
    SECRET_KEY = os.environ.get('SECRET_KEY') or csrf
    OPTIONS = config['options']
    ODOO = config['odoo']
    CRM = config['crm']
    try:
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO['host']))
        ODOO['uid'] = str(common.authenticate(ODOO['dbname'], ODOO['user'], ODOO['pwd'], {}))
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO['host']))
        CRM['team_id'] = str(models.execute_kw(ODOO['dbname'], ODOO['uid'], ODOO['pwd'],
                                         'crm.team', 'search',[[('name', '=', CRM['team'])]])[0])
    except:
        CRM['team_id'] = '0'
    SELECTION = []
    for k, v in config['selection'].items():
        SELECTION.append((k, v))