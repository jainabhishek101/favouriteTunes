from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    Title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Title