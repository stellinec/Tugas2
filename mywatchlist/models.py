from django.db import models

class MyWatchedList(models.Model):
    watched = models.CharField()
    title = models.TextField()
    rating = models.TextField()
    release_date= models.TextField()
    review = models.TextField()
    