from flask import render_template
from wolf import app

def error():
    theme = bool(app.config['OPTIONS']['wolf_theme'])
    return render_template('error.html', theme=theme, title='Error')