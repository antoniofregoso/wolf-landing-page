from flask import Flask, render_template, request, flash, redirect
from models.odoo import server
from config import Config    
from models.forms import LoginForm  , LeadForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'Miguel'}
    qs = request.args
    test = server().connection(app.config['ODOO'])
    form = LeadForm()
    if form.validate_on_submit():
        return redirect('/gracias.html')
    
    return render_template('index.html', title='Home', user=user,q=test, form=form)

@app.route('/gracias')
def gracias():
    if request.method == 'POST':
        return 'Exito'
    return 'Puto'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    
    