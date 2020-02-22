from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class LeadForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message='Se requiere tu nombre')])
    email = StringField('Correo', validators=[DataRequired(message='Se requiere tu correo'), Email(message='Puto')])
    phone = StringField('Teléfono', validators=[DataRequired(message='Se requiere tu teléfono')])
    subject = StringField('Asunto', validators=[DataRequired(message='Se requiere un asunto')])
    message = StringField('Mensaje', widget=TextArea(), validators=[DataRequired(message='Se requiere tu mensaje')])
    utm_campaign = HiddenField()
    utm_source = HiddenField()
    utm_medium = HiddenField()
    utm_term = HiddenField()
    utm_content = HiddenField()  
    category = HiddenField()  
    submit = SubmitField('Enviar')