#thank you for helping us
from google_cloud import get_abstract, text_to_speech
from markupsafe import escape
from flask import Flask, render_template, request, url_for, flash, redirect

from google_cloud import get_abstract

app = Flask(__name__, template_folder=".")

messages = [{'title': 'Message One'},
             #'content': 'Message One Content'},
            {'title': 'Message Two'}
             #'content': 'Message Two Content'}
            ]

#@app.route('/')
# def science_buddy():
#     site = "https://www.sciencedirect.com/science/article/pii/S0043135402004967"
#     abstract = get_abstract(site)
#     accent = "United Kingdom"
#     speed = "regular"
#     text_to_speech(abstract, accent, speed)
#     return '<h1>Science Buddy</h1>'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/parse', methods=['POST'])
def parse():
    paper_url = request.form['paper_url']
    abstract = get_abstract(paper_url)
    accent = "United Kingdom"
    speed = "regular"
    abstract_mp3 = text_to_speech(abstract, accent, speed)
    return f'<a href="{abstract_mp3}">Download abstract MP3 file</a>'

@app.route('/about/')
def about():
    return '<h3>Pearl Hacks 2022!</h3>'