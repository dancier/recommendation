import atexit

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler

from compute import run as do_compute

# https://stackoverflow.com/questions/16053364/make-sure-only-one-worker-launches-the-apscheduler-event-in-a-pyramid-web-app-ru
# consider switching to: https://testdriven.io/blog/flask-and-celery/
scheduler = BackgroundScheduler(
    jobstores={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')})
scheduler.remove_all_jobs()
scheduler.start()
if not scheduler.get_jobs():
    scheduler.add_job(func=do_compute, trigger="cron", hour=18)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
