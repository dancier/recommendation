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
    print("Attempting to get JWT " + str(from_multipart_payload))
    print("With: " + Config.S3_TOKENURI)
    res = requests.post(
        Config.S3_TOKENURI, data=from_multipart_payload, headers=headers
    )
    print("Got res" + str(res))
    return res.json()


class Connection:

    def connect(self):
        provider = WebIdentityProvider(jwt_provider_func=lambda: jwt(),
            sts_endpoint=Config.S3_STS_ENDPOINT,
            duration_seconds=86400
        )
        self.client = Minio(Config.S3_HOST, credentials=provider)

    def process_all(self, bucket_name):
        import importer
        for obj in self.client.list_objects(bucket_name, recursive=True):
            if not obj.is_dir:
                try:
                    response = self.client.get_object(bucket_name, obj.object_name)
                    importer.from_s3_into_db(response.data.decode())
                finally:
                    response.close()
                    response.release_conn()
