import xmlrpc.client

class server:
    
    
   
    def create_object(self,odoo, odoo_object, values):
        url = odoo['host']
        db = odoo['dbname']
        uid  = odoo['uid']
        password = odoo['pwd']
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        object_id = models.execute_kw(db, uid, password, odoo_object, 'create', [values])
        return object_id
        
    
    def get_utm(self,odoo):
        url = odoo['host']
        db = odoo['dbname']
        uid  = odoo['uid']
        password = odoo['pwd']
        utm = {}
        #Get campaign names
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        try:
            utm_campaign = models.execute_kw(db, uid, password,
                                             'utm.campaign', 'search_read',[], 
                                             {'fields': ['name']})
        except:
            utm_campaign = []
        utm['campaign'] = utm_campaign
        #Get source names
        try:
            utm_source = models.execute_kw(db, uid, password,
                                             'utm.source', 'search_read',[], 
                                             {'fields': ['name']})
        except:
            utm_source = []
        utm['source'] = utm_source
        #Get medium names
        try:
            utm_medium = models.execute_kw(db, uid, password,
                                             'utm.medium', 'search_read',[], 
                                             {'fields': ['name']})
        except:
            utm_medium = []
        utm['medium'] = utm_medium
        #Get term names
        try:
            utm_term = models.execute_kw(db, uid, password,
                                             'utm.term', 'search_read',[], 
                                             {'fields': ['name']})
        except:
            utm_term = []
        utm['term'] = utm_term
        #Get content name
        try:
            utm_content = models.execute_kw(db, uid, password,
                                             'utm.content', 'search_read',[], 
                                             {'fields': ['name']})
        except:
            utm_content = []
        utm['content'] = utm_content
        
        return utm
    
    def check_utm(self,data, values):
        res = list(filter(lambda kw: kw['name'] == data, values))
        return res
    
    def check_contact(self,odoo, res):
        url = odoo['host']
        db = odoo['dbname']
        uid  = odoo['uid']
        password = odoo['pwd']
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        try:
            res = models.execute_kw(db, uid, password,
                                                 'res.partner', 'search_read',
                                                 [['|', ('email','=', res['email']), ('email','=', res['name'])]], 
                                                 {'fields': ['name', 'email', 'phone']})[0]['id']
        except:
            res = 0
        return res
        
            
        
        
       
        
    
    
        
        
        
        
        






