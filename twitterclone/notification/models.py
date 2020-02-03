from django.db import models
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser

class Notification(models.Model):
    recipient = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.tweet