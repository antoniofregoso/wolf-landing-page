from flask import Flask, render_template, request, flash, redirect, url_for
from wolf.config import Config   
from wolf.models.forms  import LeadForm


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    qs = request.args
    form = LeadForm()
    form.selection.choices = app.config['SELECTION']
    form.utm_campaign.data = request.args.get('utm_campaign')
    form.utm_source.data =  request.args.get('utm_source')
    form.utm_medium.data=  request.args.get('utm_medium')
    form.utm_content.data = request.args.get('utm_content')
    form.utm_term.data = request.args.get('utm_term')
    theme = bool(app.config['OPTIONS']['wolf_theme'])
    if form.validate_on_submit():
        return redirect(url_for('gracias'))
    return render_template('index.html', theme=theme, title='Grupo Torreblanca|Seguros', q=qs, form=form, ga=app.config['OPTIONS']['google'], fb=app.config['OPTIONS']['facebook'])

@app.route('/gracias', methods=['GET', 'POST'])
def gracias():
    theme = bool(app.config['OPTIONS']['wolf_theme'])
    if request.method == 'POST':
        form = request.form
        return render_template('lead.html', theme=theme, title='Gracias', name= form['name'])
       
    else:
        return redirect(url_for('error'))

@app.route('/error')
def error():
    theme = bool(app.config['OPTIONS']['wolf_theme'])
    return render_template('error.html', theme=theme, title='Error')



@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml', url=app.config['OPTIONS']['url'])



if __name__ == "__main__":
    app.run(host='0.0.0.0')
    