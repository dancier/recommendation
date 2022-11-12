from flask import Flask
from database import db_session
import schedule

app = Flask(__name__)
app.config.from_object("config.Config")



@app.route("/recommendations/<dancerid>")
def recommendations(dancerid):
    res = {
        "type": "DANCER",
        "recommendationId": "string",
        "recommendationTime": "string",
        "targedId": "string",
        "targedTime": "string",
        "targetVersion": 1,
        "score": 0
    }
    return res


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()