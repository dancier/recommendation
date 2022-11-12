import atexit
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from compute import run as do_compute
from datetime import datetime
from datetime import timedelta


# https://stackoverflow.com/questions/16053364/make-sure-only-one-worker-launches-the-apscheduler-event-in-a-pyramid-web-app-ru
# consider switching to: https://testdriven.io/blog/flask-and-celery/
scheduler = BackgroundScheduler(
    jobstores={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')})
scheduler.remove_all_jobs()
scheduler.start()
scheduler.add_job(func=do_compute, trigger="cron", hour=23)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
