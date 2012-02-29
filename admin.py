from django.contrib import admin
from victr.models import *

class EventAdmin(admin.ModelAdmin):
    exclude = ['slug']
    fieldsets = ( (None, {
            'fields': ('name', 'description', 'show_results', 'rsvp',)
        }),
        ('Schedule', {
            'fields': ('scheduled', 'open', 'close', 'hidden',)
        })
    )
    list_display = ('name', 'show_results', 'is_open', 'open', 'close',)

class ProjectAdmin(admin.ModelAdmin):    
    list_display = ('title', 'event', 'url', 'rank', 'award',)
    list_filter = ('event',)
    
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(UserProfile)