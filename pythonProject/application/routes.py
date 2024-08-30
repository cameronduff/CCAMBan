from flask import render_template

from application import app
from application.data import csvReader


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/meetTheTechGrads')
def meetTheTechGrads():
    return render_template('MeetTheTechGrads.html')

@app.route('/meetTheRoles')
def meetTheRoles():
    return render_template('MeetTheRoles.html')

@app.route('/skyGlossary')
def sky_glossary():
    glossary_list = csvReader.read_csv('application/data/glossary.csv')
    return render_template('SkyGlossary.html', glossary_list=glossary_list)

@app.route('/Livingston')
def livingston():
    return render_template('Livingston.html', title='Livingston')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

