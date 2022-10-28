from flask import Flask
import schedule

app = Flask(__name__)

app.config.from_object("config.Config")

schedule.init()


@app.route("/")
def hello():
    return 'Unicorn'
