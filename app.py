from flask import Flask, render_template, request, flash, redirect, url_for
from models.odoo import server
from config import Config    
from models.forms import LeadForm
import logging

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
    return render_template('index.html', theme=theme, title='Home', q=qs, form=form, ga=app.config['OPTIONS']['google'], fb=app.config['OPTIONS']['facebook'])

@app.route('/gracias', methods=['GET', 'POST'])
def gracias():
    theme = bool(app.config['OPTIONS']['wolf_theme'])
    if request.method == 'POST':
        form = request.form
        lead = {}    
        crm = server()
        utm = crm.get_utm(app.config['ODOO']) 
        #Check campaing 
        try: 
            check = crm.check_utm(form['utm_campaign'], utm['campaign'] )[0]
            lead['campaign_id'] = check['id']
            app.logger.warning('testing warning log')
        except:
            pass
        #Check source
        try: 
            check = crm.check_utm(form['utm_source'] , utm['source'] )[0]
            lead['source_id'] = check['id']
        except:
            pass
        #Check medium
        try: 
            check = crm.check_utm(form['utm_medium'] , utm['medium'] )[0]
            lead['medium_id'] = check['id']
        except:
            pass
        #Check content
        try: 
            check = crm.check_utm(form['utm_content'] , utm['content'] )[0]
            lead['content_id'] = check['id']
        except:
            pass
        #Check term
        try: 
            check = crm.check_utm(form['utm_term'] , utm['term'] )[0]
            lead['term_id'] = check['id']
        except:
            pass
        #Add team_id
        try:
            lead['team_id'] = int(app.config['CRM']['team_id'])
        except:
            pass
        lead['description'] = form['message']
        lead['name'] = form['subject']
        lead['type'] = 'opportunity'
        lead['probability'] = app.config['CRM']['probability']
        i = 0
        j = 0
        description = "Interesado en: \n"
        for item in  form.getlist('selection'):
            for option in app.config['SELECTION']:
                if option[0]==item:
                    description += option[1] + '\n'
            i +=  float(item)
            j += 1
        lead['planned_revenue'] = i/j
        lead['description'] = description
        partner = {}
        partner['name'] = form['name']
        partner['email'] = form['email']
        partner['phone'] = form['phone']
        partner_id = crm.check_contact(app.config['ODOO'], partner)
        
        if partner_id > 0:
            lead['partner_id'] = partner_id
            lead_id = crm.create_object(app.config['ODOO'],'crm.lead', lead)
        else:
            lead['partner_id'] = crm.create_object(app.config['ODOO'],'res.partner', partner)
            lead_id = crm.create_object(app.config['ODOO'],'crm.lead', lead)        
        return render_template('lead.html', theme=theme, title='Gracias', name= form['name'])
       
    else:
        return redirect(url_for('error'))

@app.route('/error')
def error():
    theme = bool(app.config['OPTIONS']['wolf_theme'])
    return render_template('error.html', theme=theme, title='Error')

@app.route('/theme')
def theme():
    theme = bool(app.config['OPTIONS']['wolf_theme'])
    return render_template('theme.html', theme=theme, title='Theme')
    