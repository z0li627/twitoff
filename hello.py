"""Minimal Flask app"""

from flask import Flask

#Make the application
app = Flask(__name__)

#make the route
@app.route("/")

#define a function
def hello():
    return "Hello world!"

