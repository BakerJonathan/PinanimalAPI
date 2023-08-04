from flask import Blueprint, render_template


site = Blueprint('site', __name__, template_folder='index')

@site.route('/')
def home():
    return render_template('index.html')