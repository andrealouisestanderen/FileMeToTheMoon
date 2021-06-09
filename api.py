from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, json, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import subprocess
import time
import uuid
import operator
import collections

import wordCounter

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = set(['png', 'txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    #tag = uuid.uuid4()
    #message = json.dumps({"tag":str(tag)})
    #session['message'] = message
    # Delete older processed images
    for filename in os.listdir('static/'):
        if filename.startswith('blurry'):  # not to remove other images
            os.remove('static/' + filename)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and check_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            if filename.rsplit('.', 1)[1].lower() == 'txt':
                return redirect(url_for('word_counter', filename=filename))

            elif filename.rsplit('.', 1)[1].lower() == 'png':
                return redirect(url_for('processed_file', filename=filename))

    return render_template('home.html')


@app.route('/processed/<filename>')
def processed_file(filename):

    newFilename = "blurry" + str(time.time()) + ".png"
    subprocess.call(['./processImage.sh', filename, newFilename])

    return render_template('processed.html', file=newFilename)


@app.route('/wordcounter/<filename>')
def word_counter(filename):

    total_words, total_unique_words, unique_words = wordCounter.countWords(
        filename)

    unique_words = {key: val for key, val in unique_words.items() if val != 1}

    sorted_dict = sorted(
        unique_words.items(), key=lambda kv: kv[1], reverse=True)

    sorted_unique_words = collections.OrderedDict(sorted_dict)

    words = sorted_unique_words.keys()
    values = sorted_unique_words.values()

    print(list(words)[0])
    print(list(values)[0])

    return render_template('showTextFile.html', tot_w=total_words, tot_u_w=total_unique_words, words=words, values=values, file=filename)


def check_file(filename):
    return '.' in filename or filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
