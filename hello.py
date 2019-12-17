"""Minimal Flask app"""

from flask import Flask, render_template

#Make the application
app = Flask(__name__)

#make the route
@app.route("/")

#define a function
def hello():
    return "Hello world!"

#make a second route
@app.route("/about")

#make the function that goes with about
def preds():
    return render_template('about.html')
