from minio import Minio
from config import Config


def sync():
    print("Getting all events from S3 and Updates DB accordingly")
    pass

def test():
    return Config.S3_SECRET



class Connection:
    client = None

    def connect(self, host):
        self.client = Minio(host, secure=False)

    def list(self, bucket_name):
        result = list()
        for obj in self.client.list_objects(bucket_name):
            result.append(obj.object_name)
        return result
