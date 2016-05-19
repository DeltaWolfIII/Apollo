# coding=utf-8

import youtube_dl
from flask import render_template, flash, redirect, session, url_for, request, g, Markup
from app import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/userdata/', methods=['POST'])
def data():
    url = request.form['url']
    db = open("db.txt","w")
    db.write(url)
    db.close()
    return "It works!"
@app.route('/about')
def about():
    return render_template('about.html')
