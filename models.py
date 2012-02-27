from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

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
	slug = models.SlugField()
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	show_results = models.BooleanField()
	rsvp = models.URLField(
			blank=True,		
			verbose_name="RSVP",
			help_text = "A URL to the event RSVP (Eventbrite, etc.)", )
	scheduled = models.DateTimeField(
			blank=True, 
			null=True,
			help_text = "When your contest will appear publicly as a simple page \
					     with an RSVP link. Leaving this blank means that your event \
					     will appear as soon as it is saved.", )
	open = models.DateTimeField(
			help_text = "When your participants can start submitting their projects.", )
	close = models.DateTimeField(
			help_text = "When submissions will close.", )
	hidden = models.DateTimeField(			
			blank=True,
			null=True,
			help_text = "When the event, results, and hacks will go into hidden mode. \
						 Leaving this off will leave all portions of this event accessible on \
						 the \"Events\" section of the site.", )

	def __unicode__(self):
		return self.name;
		
	def is_open(self):
		# checks if current event is in the open scope
		return self.open < datetime.now() and self.close > datetime.now()
		
	def is_visible(self):
		# checks if current event is in the visible scope
		return(self.scheduled is None or self.scheduled <= datetime.now()) and (self.hidden is None or self.hidden >= datetime.now())

	def save(self):
		if not self.id:
			self.slug = SlugifyUniquely(self.name, self.__class__)
		super(self.__class__, self).save()

class Project(models.Model):
    slug          = models.SlugField()
    title         = models.CharField(max_length=50)
    description   = models.TextField(blank=True)
    url           = models.URLField(blank=True)
    event         = models.ForeignKey(Event)
    rank          = models.IntegerField(
    		            blank=True,	
    		            null=True,
                        help_text = "What place the project came in in the contest.", )
    award         = models.CharField(
    		            max_length=50,
    		            blank=True,			
                        help_text = "e.g. \"Best UX\" or \"Honorable Mention\"", )
    
    # other_urls
    # tags = models.ManyToManyField(Discipline, blank=True)
    # collaborators = models.ManyToManyField(User, blank=True)
    # screenshot = models.ImageField(upload_to="images/screenshot")

    def save(self):
        if not self.id:
            self.slug = SlugifyUniquely(self.title, self.__class__)
        super(self.__class__, self).save()
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    company = models.CharField(blank=True, max_length=40)
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField(Discipline, blank=True)
    def __unicode__(self) :
        return str(self.user)
