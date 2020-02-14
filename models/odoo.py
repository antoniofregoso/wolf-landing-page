import xmlrpc.client

class server:
    
    def connection(self, odoo):
        host = odoo['host']
        db = odoo['dbname']
        username  = odoo['user']
        password = odoo['pwd']
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(host))
        return common.version()
        
        
        






