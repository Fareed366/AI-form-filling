from flask import Flask, request, render_template, send_from_directory
from flask_bootstrap import Bootstrap 
import os
from pickle import load
from numpy import argmax
import os
import pytesseract as tess
from PIL import Image
import pyttsx3

language="en"
mytext="hello world"
engine = pyttsx3.init()
paths=None
x=[None,None,None,None]
i=0
description=None
PEOPLE_FOLDER = os.path.join('static', 'img')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route("/final",methods=["POST"])
def final():
    return render_template("rr.html")

@app.route('/show')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], path)
    photo = full_filename
    img = Image.open(photo)
    global description
    description = tess.image_to_string(img)
    tt=description.split("\n")
    t=[string for string in tt if string!='' and string!=' ']
    t.pop(0)
    print(t)
    for i in t:
        engine.say(i)	
	
    print("hii")
    
    return render_template("index.html",description=t)

@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/img/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        filename = upload.filename
        ext = os.path.splitext(filename)[1]
        if (ext == ".csv"):
            print("File supported moving on...")
        else:
            print("error")
        destination = "/".join([target, filename])
        upload.save(destination)
    global path
    path=filename
    return render_template("complete.html", image_name=filename)




if __name__ == '__main__':
	app.run(debug=True)

