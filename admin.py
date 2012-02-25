from django.contrib import admin
from victr.models import Event

class EventAdmin(admin.ModelAdmin):
    exclude = ['slug']
    fieldsets = ( (None, {
            'fields': ('name', 'description', 'show_results', 'rsvp')
        }),
        ('Schedule', {
            'fields': ('scheduled', 'open', 'close', 'hidden')
        })
    )

admin.site.register(Event, EventAdmin)