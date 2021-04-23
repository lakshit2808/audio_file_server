from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    Name = models.CharField(max_length=100)
    Song = models.FileField(upload_to='Song/')
    Duration = models.PositiveIntegerField()
    Upload_date = models.DateTimeField()

    def __str__(self):
        return self.Name


class Podcast(models.Model):
    Name = models.CharField(max_length=100)
    Podcast = models.FileField(upload_to='Podcast/')
    Duration = models.PositiveIntegerField()
    Upload_date = models.DateTimeField()
    Host = models.CharField(max_length=100)
    Participants = models.ManyToManyField(User , related_name='Participants')

    def __str__(self):
        return self.Name

class AudioBook(models.Model):
    Title = models.CharField(max_length=100)
    AudioBook = models.FileField(upload_to='Audiobook/')
    Author = models.CharField(max_length=100)
    Narrator = models.CharField(max_length=100)
    Duration = models.PositiveIntegerField()
    Upload_date = models.DateTimeField()

    def __str__(self):
        return self.Title
    

