from django.contrib.auth.models import User
from django.db import models

class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', symmetrical=False)


    def __str__(self):
        return self.user.username