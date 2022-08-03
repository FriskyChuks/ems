from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api2

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_api2,'interval', seconds=6)
    scheduler.start()

