# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, HiddenField, SelectMultipleField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea, CheckboxInput, ListWidget

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

    
class LeadForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message='Se requiere tu nombre')])
    email = StringField('Correo', validators=[DataRequired(message='Se requiere tu correo'), Email(message='Puto')])
    phone = StringField(u'Teléfono', validators=[DataRequired(message='Se requiere tu teléfono')])
    selection = MultiCheckboxField('Me interesa', validators=[DataRequired(message='Seleccione')])
    subject = StringField('Asunto', validators=[DataRequired(message='Se requiere un asunto')])
    message = StringField('Mensaje', widget=TextArea(), validators=[DataRequired(message='Se requiere tu mensaje')])
    utm_campaign = HiddenField()
    utm_source = HiddenField()
    utm_medium = HiddenField()
    utm_term = HiddenField()
    utm_content = HiddenField() 
    submit = SubmitField('Enviar')