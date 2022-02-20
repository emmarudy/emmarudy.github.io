from google_cloud import get_abstract, text_to_speech
from markupsafe import escape
from flask import Flask, render_template, request, url_for, flash, redirect

from google_cloud import get_abstract

app = Flask(__name__)

messages = [{'title': 'Message One'},
             #'content': 'Message One Content'},
            {'title': 'Message Two'}
             #'content': 'Message Two Content'}
            ]

@app.route('/')
# def science_buddy():
#     site = "https://www.sciencedirect.com/science/article/pii/S0043135402004967"
#     abstract = get_abstract(site)
#     accent = "United Kingdom"
#     speed = "regular"
#     text_to_speech(abstract, accent, speed)
#     return '<h1>Science Buddy</h1>'

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        #content = request.form['content']

        if not title:
            flash('Title is required!')
        # elif not content:
        #     flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/index/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'