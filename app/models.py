from django.db import models
from django.utils import timezone

# Create your models here.
class Activity(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.TextField()
    dateCreated = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
