import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_news_crawler.settings')

# creating celery app
app = Celery('django_news_crawler')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# configure celery beat to update the weather every 30 minutes
app.conf.beat_schedule = {
    # Scheduler Name
    'crawl-news-thirty-minutes': {
        # Task Name (Name Specified in Decorator)
        'task': 'get_weather_data',
        # Schedule
        'schedule': 1800.0,
        # Function Arguments
        'args': ()
    },
}


# Commands:
# $ celery -A weather_service worker -l info --pool=solo
# $ celery -A weather_service beat -l info
