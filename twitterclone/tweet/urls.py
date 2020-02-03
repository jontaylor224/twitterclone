from django.urls import path
from twitterclone.tweet.views import create_tweet, tweet_detail

urlpatterns = [
    path('addtweet/', create_tweet, name='addtweet'),
    path('tweet/<int:tweet_id>', tweet_detail, name='tweet_detail')
]

