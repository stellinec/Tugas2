from django.db import models

class MyWatchedList(models.Model):
    watched = models.CharField(max_length=255)
    title = models.TextField()
    rating = models.TextField()
    release_date= models.TextField()
    review = models.TextField()
    