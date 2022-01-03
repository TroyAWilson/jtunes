from os import environ
from flask import Flask, render_template, url_for, request
import requests
import json
import random

app = Flask(__name__)

@app.route('/')
def index():
    batch = requests.get(f'https://itunes.apple.com/search?term=Gorillaz').json()
    return render_template('home.html', batch = batch['results'])



@app.route('/getNewMusic', methods = ['GET', 'POST'])
def getNewMusic():
    if request.method == "POST":
        name = request.form.get('newName')
        return musicByName(name)
    return "uh oh, something went wrong"


@app.route('/music/<name>')
def musicByName(name = None):
    r = requests.get(f'https://itunes.apple.com/search?term={name}').json()
    
    print(r['results'][0])

    out = []
    for i in r['results']:
        if i['artistName'].lower() == name.lower():
            out.append(i)
    
    return render_template('home.html', batch = out)


if __name__ == '__main__':
    app.run()