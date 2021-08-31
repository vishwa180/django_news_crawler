Django News Craler
--------------

1. Running Django Server::

    $ pip3 install -r requirements.txt
    $ py manage.py makemigrations
    $ py manage.py migrate
    $ py manage.py runserver

2. Install and run RabbitMQ Server via Docker:
    docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 8080:15672 rabbitmq:3-management

3. Running Celery Worker:
    $ celery -A django_news_crawler worker -l info --pool=solo

4. Running Celery Beat:
    $ celery -A django_news_crawler beat -l info
