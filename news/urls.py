from django.urls import path
from . import views


urlpatterns = [
    # get news articles api
    path('/', views.NewsView.as_view())
]
