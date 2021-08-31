from celery import shared_task
from celery.utils.log import get_task_logger
from . import models
from bs4 import BeautifulSoup
import requests

logger = get_task_logger(__name__)


# crawl and store news data from hacker news website
# run this every 30 minutes
@shared_task(name="crawl_news_data")
def crawl_news_data():
    logger.info("Getting news data")

    # make a GET request to get the entire HTML page
    page = requests.get('https://news.ycombinator.com/newest')
    soup = BeautifulSoup(page.content, 'html.parser')

    # get all the news links (news links in hacker news have a class called "storylink")
    story_links = soup.find_all('a', {'class': 'storylink'})

    # loop through the links and create a record in database
    for link in story_links:
        url = link.get('href')

        # the news articles are sorted by time and when a pre-existing news comes, we can stop the loop
        if models.NewsArticle.objects.filter(url=url).exists():
            break

        # creating a NewsArticle object and storing into database
        title = link.get_text()
        models.NewsArticle.objects.create(title=title, url=url)
