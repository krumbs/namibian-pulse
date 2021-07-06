from flask import Flask
from datetime import datetime
from flask import render_template
import re


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Namibia!"

@app.route("/hello/")
@app.route("/hello/<name>")
def welcome_user(name=None):
    return render_template(
        "welcome.html",
        name=name,
        date=datetime.now()
    )
    