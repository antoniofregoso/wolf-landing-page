from flask import Flask, render_template, request, flash, redirect
from odoo import server
from config import Config    
from forms import LoginForm  
from odoo import server

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    test = server().connection()
    qs = request.args
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        version = server.connection(self)
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    
    