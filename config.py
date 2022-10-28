import os

basedir = os.path.abspath(__file__)


class Config(object):
    S3_SECRET = os.getenv("S3_SECRET","SECRET")