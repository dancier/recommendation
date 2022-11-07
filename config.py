import os

basedir = os.path.abspath(__file__)


class Config(object):
    S3_SECRET = os.getenv("S3_SECRET", "SECRET")
    S3_TOKENURI = os.getenv("S3_TOKENURI", "https://iam.dancier.net/realms/dancier/protocol/openid-connect/token")
    S3_STS_ENDPOINT = os.getenv("S3_STS_ENDPOINT", "https://s3.dancier.net")
    S3_HOST = os.getenv("S3_HOST", "s3.dancier.net")
    S3_BUCKET = os.getenv("S3_BUCKET", "lake")
    DB_USER = os.getenv("DB_USER", "recommendation")
    DB_PASS = os.getenv("DB_PASS", "recommendation")
    DB_NAME = os.getenv("DB_NAME", "recommendation")
    DB_HOST = os.getenv("DB_HOST", "localhost")
