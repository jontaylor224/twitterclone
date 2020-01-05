from django.db import models
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser

class Notification(models.Model):
    notification_unread = models.BooleanField(default=True)
    notification_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    notification_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.notification_tweet