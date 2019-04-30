# Code adapted from https://pythonspot.com/flask-web-forms/

import os, sys
import datetime
# import pymongo
import pandas as pd
import numpy as np

from flask import Flask, render_template, flash, request
from wtforms import Form, SelectField, TextField, TextAreaField, validators, StringField, SubmitField
import win_expectancy


# App config.
DEBUG = True
app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def checkbox(id):
    try:
        value = request.form[id]
        value = 1
    except:
        value = 0
    return value


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = request.form

    if request.method == 'POST':

        df1518 = win_expectancy.readData_Court()
        gameData = df1518.copy().groupby(['game_date', 'away_team', 'home_team']).max()[['away_score', 'home_score']].reset_index()
        gameData['W'] = gameData['home_score']>gameData['away_score']
        states = df1518.copy()
        df = states.merge(gameData[['game_date','home_team','W']], how='inner',on=['game_date', 'home_team'])
        ranking = pd.read_csv('../../data/rankings.csv') #https://www.baseball-reference.com/leagues/MLB/2018-standings.shtml

        b_team_home = request.form['b_team_home']
        b_team_away = request.form['b_team_away']
        b_home_score = request.form['b_home_score'] 
        b_away_score = request.form['b_away_score']
        b_inning = request.form['b_inning']
        b_top_bot = request.form['b_top_bot']
        b_outs = request.form['b_outs']

        b_on_1b = checkbox('b_on_1b')
        b_on_2b = checkbox('b_on_2b')
        b_on_3b = checkbox('b_on_3b')


        # team_home = request.form['team_home'] # key value pairs
        # team_away = request.form['team_away']
        home_score = request.form['home_score']
        away_score = request.form['away_score']
        outs = request.form['outs']

        on_1b = checkbox('on_1b')
        on_2b = checkbox('on_2b')
        on_3b = checkbox('on_3b')

        probBefore = win_expectancy.getState(df, int(b_inning), b_top_bot, b_on_1b, b_on_2b, b_on_3b, int(b_outs), int(b_home_score)-int(b_away_score))
        probCurrent = win_expectancy.getState(df, int(b_inning), b_top_bot, on_1b, on_2b, on_3b, int(outs), int(home_score)-int(away_score))
        if b_top_bot == 'Bot':
            r = win_expectancy.getRank(ranking, b_team_home)
        else:
            r = win_expectancy.getRank(ranking, b_team_away)
        newProb = win_expectancy.getWeight(probBefore, probCurrent, r)
        flash(newProb)

    
    return render_template('hello.html', form=form)


# @app.route("/people/", methods=['GET', 'POST'])
# def people():
#     form = ReusableForm(request.form)
#     personarr = retrieve_from_db.getAll() #returns all people in the database
#     personarr.sort()
#     alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     # letter = request.form['name']
#     # print (letter)
#     # person = retrieve_from_db.searchByLetter(letter)
#     return render_template('people.html', person = person, people = personarr, alphabet=alphabet)

# 
# @app.route("/edit/", methods=['GET', 'POST'])
# def edit():
#     form = ReusableForm(request.form)
#     name = request.args.get('name')
#     person = retrieve_from_db.getOneforDisplay(name)
#     if request.method == 'POST':
#         name = request.form['name'] # key value pairs
#         degree = request.form['degree']
#         occupation = request.form['occupation']
#         icon = request.files['icon']
#         image1 = request.files['image1']
#         paragraph1 = request.form['paragraph1']
#         image2 = request.files['image2']
#         paragraph2 = request.form['paragraph2']
#         image3 = request.files['image3']
#         paragraph3 = request.form['paragraph3']
#         category = request.form['category']
#         hidden = checkbox('hidden')
# 
#         icon_filename = image(icon, name + '_icon.jpg')
#         image1_filename = image(image1, name + '_image1.jpg')
#         image2_filename = image(image2, name + '_image2.jpg')
#         image3_filename = image(image3, name + '_image3.jpg')
# 
#         if form.validate():
#             flash(person['name'])
#             edit_person.editOne(person['_id'], name, degree, occupation, icon_filename, image1_filename, paragraph1,
#                             image2_filename, paragraph2, image3_filename, paragraph3, category, hidden)
#             print("edit to database successful")
#         else:
#             flash('All the form fields are required.')
#     return render_template('edit.html', person=person, form=form)
# 
# 
# @app.route("/person/", methods=['GET', 'POST'])
# def person():
#     name = request.args.get('name')
#     person = retrieve_from_db.getOneforDisplay(name)
#     # dbFileName = retrieve_from_db.getPhotoFileName(person['icon'])
#     retrieve_from_db.getPhoto(person['name']+'_icon.jpg')
#     retrieve_from_db.getPhoto(person['name']+'_image1.jpg')
#     if (person['image2']):
#         retrieve_from_db.getPhoto(person['name']+'_image2.jpg')
#     if (person['image3']):
#         retrieve_from_db.getPhoto(person['name']+'_image3.jpg')
# 
#     return render_template('person.html', person=person)
# 
# 
# @app.route("/display/", methods=['GET', 'POST'])
# def display():
#     tabsarr =[]
#     tabsarr.append(retrieve_from_db.getAllContent('category', 'tab'))
#     peoplecatarr=[] #array to hold the categories of people
#     peoplecatarr.append(retrieve_from_db.getAllContent('category', 'people'))
#     historycatarr=[] #array to hold the categories of history
#     historycatarr.append(retrieve_from_db.getAllContent('category', 'history'))
#     athleticscatarr=[] #array to hold the categories of athletics
#     athleticscatarr.append(retrieve_from_db.getAllContent('category', 'athletics'))
#     athletesarr=[]
#     astronautsarr=[]
#     athletesarr.append(retrieve_from_db.getAllContent('category','athletes'))
#     astronautsarr.append(retrieve_from_db.getAllContent('category','astronauts'))
#     # peoplecatarr.sort()
#     athletesarr.sort()
#     astronautsarr.sort()
#     return render_template('display.html', tabsarr=tabsarr, athleticscatarr = athleticscatarr, historycatarr = historycatarr, peoplecatarr=peoplecatarr,  athletesarr=athletesarr, astronautsarr=astronautsarr)
# 
# @app.route("/search/", methods=['GET', 'POST'])
# def search():
#     form = ReusableForm(request.form)
#     print (form.errors)
#     alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
#     bet = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     person = []
#     toFind = {}
#     if request.method == 'POST':
#         try:
#             letter = request.form['name']
#             print (letter)
#             person = retrieve_from_db.searchByLetter(letter)
#         except:
#             toFind['name'] = ''
#         try:
#             toFind['school'] = request.form['school']
#             person = retrieve_from_db.getOne(toFind)
#         except:
#             toFind['school'] = ''
#         try:
#             toFind['year'] = request.form['year']
#             person = retrieve_from_db.getOne(toFind)
#         except:
#             toFind['year'] = ''
#     # person = retrieve_from_db.getOne(toFind)
#     return render_template('search.html', form=form, person=person, alpha=alpha, bet=bet)


if __name__ == "__main__":
    app.run()
