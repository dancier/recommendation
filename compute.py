import s3
import datetime
from config import Config
from os import getpid
from dao import PairsDao


def run():
    start_of_sync = datetime.datetime.now()
    print("Fetching current state from S3: " + str(getpid()))
    con = s3.Connection()
    con.connect()
    con.process_all(Config.S3_BUCKET)
    end_of_sync = datetime.datetime.now()
    print("Processing time: "
          + str(end_of_sync - start_of_sync)
          + " on worker: " + str(getpid()))

    print("Computing the pairs...")
    PairsDao.generate_pairs()

    PairsDao.do_for_all()
    print("Storing results in database")
