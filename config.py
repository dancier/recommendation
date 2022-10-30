import os

basedir = os.path.abspath(__file__)


class Config(object):
    S3_SECRET = os.getenv("S3_SECRET","SECRET")
    S3_TOKENURI = os.getenv("S3_TOKENURI", "https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/token")
    S3_HOST = os.getenv("S3_HOST", "https://test-s3.dancier.net")
    S3_BUCKET = os.getenv("S3_BUCKET", "lake")
