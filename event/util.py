from datetime import datetime
from victr.models import Event, Schedule

def currentEvent():
    events = Event.objects.exclude(schedule__hidden__lte=datetime.now()).order_by('schedule__open')
    # logic here!
    
    return e