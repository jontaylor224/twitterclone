from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils import timezone
from twitterclone.twitteruser.models import TwitterUser

class Tweet(models.Model):
    content = models.CharField(max_length=140, null=True, blank=True, validators=[MaxLengthValidator(140)])
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
