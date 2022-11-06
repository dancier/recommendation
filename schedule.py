import atexit
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from compute import run as do_compute
from datetime import datetime
from datetime import timedelta


# https://stackoverflow.com/questions/16053364/make-sure-only-one-worker-launches-the-apscheduler-event-in-a-pyramid-web-app-ru
# consider switching to: https://testdriven.io/blog/flask-and-celery/
def init():
    scheduler = BackgroundScheduler(
        jobstores={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')})
    scheduler.start()
    scheduler.add_job(func=do_compute, trigger="interval", next_run_time=datetime.now() + timedelta(seconds=5),
                      seconds=600
                      )
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
