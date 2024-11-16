from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about1')
def about():
    return render_template('about.html')

@app.route('/newby')
def new_page():
    return render_template('new_page11.html')

