activate_this = '/var/www/torreblanca/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from wolf import app as aplication


import sys
sys.path.insert(0, '/var/www/torreblanca/wolf')