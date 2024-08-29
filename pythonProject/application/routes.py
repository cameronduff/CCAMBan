from flask import render_template

from application import app

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
def skyGlossary():
    return render_template('SkyGlossary.html')