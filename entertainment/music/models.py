from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200, blank=True,null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    votes = models.IntegerField(default=0, blank=True, null=True)
    logo = models.URLField(max_length=200, blank=True, null=True)
    members = models.CharField(max_length=500, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    youtube = models.URLField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    chart = models.IntegerField(default=0, blank=True, null=True)
    award = models.CharField(max_length=200, blank=True, null=True)
    release_year = models.DateField(blank=True, null=True)
    cover = models.URLField(max_length=500, blank=True, null=True)
    votes = models.IntegerField(default=0, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    chart = models.IntegerField(default=0, blank=True, null=True)
    award = models.CharField(max_length=200, blank=True, null=True)
    chart_date = models.DateField(blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)
    votes = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name
