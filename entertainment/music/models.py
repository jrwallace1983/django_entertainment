from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    votes = models.IntegerField(default=0)
    logo = models.URLField(max_length=200, null=True)
    members = models.CharField(max_length=500, null=True)
    summary = models.TextField()
    slug = models.SlugField(unique=True)
    youtube = models.URLField(max_length=300, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    chart = models.IntegerField(default=0)
    award = models.CharField(max_length=200)
    release_year = models.DateField()
    cover = models.URLField(max_length=500)
    votes = models.IntegerField(default=0)
    youtube = models.URLField(max_length=500, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    chart = models.IntegerField(default=0)
    award = models.CharField(max_length=200)
    chart_date = models.DateField()
    youtube = models.URLField(max_length=500)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
