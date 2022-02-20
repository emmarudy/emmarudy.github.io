#thank you for helping us
from google_cloud import get_abstract, text_to_speech
from markupsafe import escape
from flask import Flask, render_template, request, url_for, flash, redirect

from google_cloud import get_abstract

app = Flask(__name__, template_folder=".", static_folder='static')

@app.route('/')
def index():
    #abstract_mp3 = ["abstract_mp3.mp3"]
    return render_template('index.html')#, abstract_mp3=abstract_mp3)

@app.route('/parse', methods=['POST', 'GET'])
def parse():
    paper_url = request.form['paper_url']
    abstract = get_abstract(paper_url)
    accent = "United Kingdom" #request.form
    speed = "regular"
    abstract_mp3 = text_to_speech(abstract, accent, speed)
    #return render_template('audio.html', abstract_mp3=abstract_mp3)
    return render_template('audio.html')
    #f'''<a href="{abstract_mp3}">Download abstract MP3 file</a>
    # <p>{abstract}</p>
    # '''

@app.route('/about/')
def about():
    return '<h3>Pearl Hacks 2022!</h3>'