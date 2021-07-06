from flask import Flask
from datetime import datetime
import re


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Namibia!"

@app.route("/hello/<name>")
def welcome_user(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Welcome " + clean_name + ". It's " + formatted_now
    return content