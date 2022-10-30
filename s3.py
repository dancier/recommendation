import requests
from minio import Minio
from minio.credentials import WebIdentityProvider

from config import Config


def jwt():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    from_multipart_payload = {
        "client_id": "s3",
        "client_secret": Config.S3_SECRET,
        "grant_type": "client_credentials"
    }
    return requests.post(
        Config.S3_TOKENURI, data=from_multipart_payload, headers=headers
    ).json()


class Connection:
    client = None

    def connect(self):
        provider = WebIdentityProvider(jwt_provider_func=lambda: jwt(),
            sts_endpoint="https://test-s3.dancier.net",
            duration_seconds=86400
        )
        self.client = Minio("test-s3.dancier.net:443", credentials=provider)

    def list(self, bucket_name):
        result = list()
        for obj in self.client.list_objects(bucket_name, recursive=True):
            result.append(obj.object_name)
        return result
