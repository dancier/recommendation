import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from compute import run as do_compute
from datetime import datetime
from datetime import timedelta


def init():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=do_compute, trigger="interval", next_run_time=datetime.now() + timedelta(seconds=5),
                      seconds=600
                      )
    scheduler.start()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
