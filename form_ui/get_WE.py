# Code adapted from https://pythonspot.com/flask-web-forms/

import os, sys
import datetime
# import pymongo
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

class ReusableForm(Form):
    name = TextField('Title: ', validators=[validators.required()])
    degree = TextField('Subtitle: ')
    occupation = TextField('Heading:')


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        team_home = request.form['team_home'] # key value pairs
        team_away = request.form['team_away']
        inning = request.form['inning']
        top_bot = request.form['top_bot']
        outs = request.form['outs']

        on_1b = checkbox('on_1b')
        on_2b = checkbox('on_2b')
        on_3b = checkbox('on_3b')

        # saving all images into folder and getting filenames

        if form.validate():
            win_expectancy.getState(0, inning, top_bot, on_1b, on_2b, on_3b, outs)
            print("HELLOOO?")
        else:
            flash('The title field is required.')
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
