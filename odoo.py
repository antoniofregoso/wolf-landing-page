import configparser
import xmlrpc.client

class server:
    
    def connection(self):
        config = configparser.ConfigParser()
        config.read('wolf.ini')
        host = config['odoo']['host']
        dbname = config['odoo']['dbname']
        user  = config['odoo']['user']
        pwd = config['odoo']['pwd']
        info = xmlrpc.client.ServerProxy(host).start()
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(host))
        return common.version()
        
        
        






