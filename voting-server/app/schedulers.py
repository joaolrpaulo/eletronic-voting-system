from apscheduler.schedulers.background import BackgroundScheduler

from app import config, models


scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_job(models.Blacklist.delete, 'interval', seconds = config.tokens.ttl)

