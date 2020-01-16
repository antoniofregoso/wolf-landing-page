from flask import Flask, render_template, request
from odoo import server
from config import Config      

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    test = server().connection()
    qs = request.args
    return render_template('index.html', user = test, q=qs)

if __name__ == '__main__':
    app.run(debug=True)
    
    