import configparser

class server:
    
    def connection(self):
        config = configparser.ConfigParser()
        config.read('wolf.ini')
        host = config['odoo']['host']
        dbname = config['odoo']['dbname']
        user  = config['odoo']['user']
        pwd = config['odoo']['pwd']
        return {'host':host, 'dbname':dbname, 'user':user, 'pwd':pwd}
        
        
        






