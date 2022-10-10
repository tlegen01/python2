import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return"<h1>index!!!</h1>"

@app.route("/products/")
def products():
    return"<h1>products!!!</h1>"

@app.route("/video_study/")
def video_study():
    return "<h1>Video</h1>"

################################

@app.route('/login', method=['GET'])
def login():
    return flask.render_template('login.html')