from django.db import models
from django.contrib.auth.models import User
from victr.util import *

# Create your models here.

class Discipline(models.Model):
    name = models.CharField(max_length=40)

    def save(self):
        if not self.id:
            self.name = SlugifyUniquely(self.name, self.__class__, 'name')
        super(self.__class__, self).save()

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True) #this should be a WYSIWYG Field
    creator = models.ForeignKey(User, blank=True)
    rsvp = models.URLField(blank=True)

class Project(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Discipline, blank=True)
    mainUrl = models.URLField()
    collaborators = models.ManyToManyField(User, blank=True)
    screenshot = models.ImageField(upload_to="images", blank=True) #this should be images/<event_id>/screenshots
    def save(self):
        if not self.id:
            self.slug = SlugifyUniquely(self.name, self.__class__)
        super(self.__class__, self).save()
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    company = models.CharField(blank=True, max_length=40)
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField(Discipline, blank=True)
    
class Rank(models.Model):
    project = models.ForeignKey(Project)
    rank = models.IntegerField(blank=True)

#class Schedule(models.Model):
