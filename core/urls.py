from django.urls import path
from rest_framework.authtoken import views as auth_views
from . import views


urlpatterns = [
    # login and logout apis
    path('obtain-token/', auth_views.obtain_auth_token),
    path('delete-token/', views.DeleteToken.as_view()),
]
