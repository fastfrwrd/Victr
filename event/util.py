from django.db.models import Q
from datetime import datetime, timedelta
from victr.models import Event, Schedule

class EventQuery:

    def all():
        """
        Returns ALL events, including invisible ones. Careful...
        """
        return Event.objects.order_by('-schedule__close')
    
    def visible():
        """
        Returns all events that are visible.
        """
        return Event.objects.filter( 
            Q(schedule__scheduled__lte = datetime.now()) | Q(schedule__scheduled__isnull = True),
            Q(schedule__hidden__gte = datetime.now()) | Q(schedule__hidden__isnull = True),
        ).order_by('-schedule__close')
        
    def current():
        """
        Returns the current event that project submissions goes to and that the
        front page will display, or returns false if there's no current event.
        """
        try :
            return Event.objects.filter(
                # visible
                Q(schedule__scheduled__lte = datetime.now()) | Q(schedule__scheduled__isnull = True),
                Q(schedule__hidden__gte = datetime.now()) | Q(schedule__hidden__isnull = True),
                # is open or closed less than 48 hours ago
                schedule__close__lte = datetime.now() + timedelta(days = 2),
            ).order_by('-schedule__close')[0]
        except IndexError:
            return False