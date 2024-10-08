from flask import render_template, redirect, url_for
from application import app
from application.data import csvReader

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/meetTheGrads')
def meetTheGrads():
    return render_template('MeetTheGrads.html', title='Meet The Grads')

@app.route('/meetTheStaff')
def meetTheStaff():
    return render_template('MeetTheStaff.html', title='Meet The Staff')

@app.route('/meetTheRoles')
def meetTheRoles():
    return render_template('MeetTheRoles.html', title='Potential Roles')

@app.route('/skyKnowledgeBank')
def sky_knowledge_bank():
    glossary_list = csvReader.read_csv('application/data/glossary.csv')
    tags = csvReader.find_tags('application/data/glossary.csv')
    return render_template('SkyKnowledgeBank.html', glossary_list=glossary_list, tags=tags, title='Sky Knowledge Bank')

@app.route('/Livingston')
def livingston():
    return render_template('Livingston.html', title='Livingston')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/agile')
def agile():
    return render_template('agile.html', title='Agile Methodologies')

@app.route('/bigdecision')
def bigdecision():
    return render_template('the_big_decision.html', title='The Big Decision')

@app.route('/Osterley')
def Osterley():
    return render_template('Osterley.html', title='Osterley')

@app.route('/Leeds')
def Leeds():
    return render_template('Leeds.html', title='Leeds')

@app.route('/gitBasics')
def git_basics():
    return render_template('gitBasics.html', title='Git Basics')

@app.route('/NewNotifications')
def notifications():
    return render_template('NewNotifications.html', title='Notifications')

@app.route('/NIST')
def NIST():
    return render_template('NIST.html', title='NIST')

@app.route('/advice')
def advice():
    return render_template('advice.html', title='Advice')