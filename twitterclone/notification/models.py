from django.db import models

class Notification(models.Model):
    notification = models.CharField()
    user = models.ForeignKey('TwitterUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.notification