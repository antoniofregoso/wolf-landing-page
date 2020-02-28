import xmlrpc.client

class server:
    
   
    def set_lead(self,odoo, values):
        url = odoo['host']
        db = odoo['dbname']
        username  = odoo['user']
        password = odoo['pwd']
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        id = models.execute_kw(db, 1, password, 'res.partner', 'create', [values])
        return id
        
    def set_opportunity(self,odoo, values):
        url = odoo['host']
        db = odoo['dbname']
        username  = odoo['user']
        password = odoo['pwd']
        return 'd'
    
    
        
        
        
        
        






