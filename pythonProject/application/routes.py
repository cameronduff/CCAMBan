from flask import render_template

from application import app
from application.data import csvReader

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/meetTheGrads')
def meetTheGrads():
    return render_template('MeetTheGrads.html')

@app.route('/meetTheRoles')
def meet_the_roles():
    return render_template('MeetTheRoles.html')

@app.route('/skyGlossary')
def sky_glossary():
    glossary_list = csvReader.read_csv('application/data/glossary.csv')
    tags = csvReader.find_tags('application/data/glossary.csv')
    return render_template('SkyGlossary.html', glossary_list=glossary_list, tags=tags)

@app.route('/Livingston')
def livingston():
    return render_template('Livingston.html', title='Livingston')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/agile')
def agile():
    return render_template('agile.html', title='Agile Methodologies')

@app.route('/bigdecision')
def bigdecision():
    return render_template('the_big_decision.html', title='The Big Decision ')