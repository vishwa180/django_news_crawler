import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_news_crawler.settings')

# creating celery app
app = Celery('django_news_crawler')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# configure celery beat to crawl for news every 30 minutes
app.conf.beat_schedule = {
    # Scheduler Name
    'crawl-news-thirty-minutes': {
        # Task Name (Name Specified in Decorator)
        'task': 'crawl_news_data',
        # Schedule
        'schedule': 1800.0,
        # Function Arguments
        'args': ()
    },
}


# Commands:
# $ celery -A django_news_crawler worker -l info --pool=solo
# $ celery -A django_news_crawler beat -l info
