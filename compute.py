import s3
import datetime
from config import Config


def run():
    start_of_sync = datetime.datetime.now()
    print("Fetching current state from S3")
    con = s3.Connection()
    con.connect()
    con.process_all(Config.S3_BUCKET)
    end_of_sync = datetime.datetime.now()
    print("Processing time: " + str(end_of_sync - start_of_sync))

    print("Computing new matches")
    print("Storing results in database")
