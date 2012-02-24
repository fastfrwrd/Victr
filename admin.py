from django.contrib import admin
from victr.models import Event, Schedule

class ScheduleInline(admin.StackedInline):
    model = Schedule
    max_num = 1

class EventAdmin(admin.ModelAdmin):
    exclude = ['slug']
    inlines = [ScheduleInline]
    pass
admin.site.register(Event, EventAdmin)