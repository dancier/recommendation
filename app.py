from flask import Flask
from database import db_session
import schedule

app = Flask(__name__)

app.config.from_object("config.Config")

schedule.init()


@app.route("/recommendations/<dancerid>")
def recommendations(dancerid):
    return dancerid


@app.route("/")
def hello():
    return 'Unicorn'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()