__author__ = 'sexybeast'

from crontab import CronTab

cron = CronTab()
job = cron.new()
job.minute()


