"""
Main app
"""
import os

from flask import Flask, render_template, redirect, request, flash


app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        print request.files
        #if 'file' not in request.files:
        #    flash("No file part!")
        #    return redirect(request.url)
        print request.files.keys()
        for file_ in request.files.itervalues():
            file_.save(os.path.join('.', file_.filename))

    return ''
