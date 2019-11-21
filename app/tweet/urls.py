from django.urls import path, include
from app.tweet import views as tweet_app_views


urlpatterns = [
    # System User Related URLs
    path('', view=tweet_app_views.tweet_list, name='tweet_list'),
    path('<int:pk>', view=tweet_app_views.tweet_details, name='tweet_details'),
]
