import flask
from flask import Flask

app = Flask(__name__)


# MVC - Model View Controller

@app.route("/index")
def index():
    return "<h1>index!!!</h1>"


@app.route("/about", methods=['GET'])
def home1():
    return flask.render_template('home1.html')


@app.route('/')  # , methods=['GET']
def home():
    context = {
        "task_list": [
            {"title": "Pomyt kota", "Description": "Nuzhno horosho pomyt kota", "status": True},
            {"title": "Pomyt sobaku", "Description": "Nuzhno horosho pomyt sobaku", "status": False},
            {"title": "Kupit slona", "Description": "Nuzhno kupit dorogogo slona", "status": True},
            {"title": "Pomyt kota", "Description": "Nuzhno horosho pomyt kota", "status": True},
            {"title": "Pomyt sobaku", "Description": "Nuzhno horosho pomyt sobaku", "status": False},
            {"title": "Kupit slona", "Description": "Nuzhno kupit dorogogo slona", "status": True},
            {"title": "Pomyt kota", "Description": "Nuzhno horosho pomyt kota", "status": True},
            {"title": "Pomyt sobaku", "Description": "Nuzhno horosho pomyt sobaku", "status": False}

        ],
        "username": "Roman"
    }
    return flask.render_template('login.html', **context)
