from flask import render_template

from application import app
from application.data import csvReader

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/meetTheTechGrads')
def meet_the_tech_grads():
    return render_template('MeetTheTechGrads.html')

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