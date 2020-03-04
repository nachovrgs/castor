import datetime

from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

