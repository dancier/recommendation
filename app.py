from flask import Flask
from database import db_session
from prometheus_flask_exporter import PrometheusMetrics
from dao import PairsDao
from schedule import scheduler

app = Flask(__name__)
app.config.from_object("config.Config")
metrics = PrometheusMetrics(app)


@app.route("/recommendations/<dancerid>")
def recommendations(dancerid):
    return PairsDao.lookup_partners(dancerid)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()