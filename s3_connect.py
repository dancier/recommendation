from minio import Minio


class Connection:
    client = None

    def connect(self, host):
        self.client = Minio(host, secure=False)

    def list(self, bucket_name):
        result = list()
        for obj in self.client.list_objects(bucket_name):
            result.append(obj.object_name)
        return result
