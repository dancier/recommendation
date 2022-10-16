from s3_connect import Connection as S3Connection
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello Felix'


@app.route("/s3")
def getBucketContent():
    s3_connection = S3Connection()
    s3_connection.connect("s3:9000")
    return s3_connection.list("test")
