from django.contrib.auth.models import User
from django.db import models


class TwitterUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    follows = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.user.username
