from django.db.models import Q
from datetime import timedelta
from django.utils.timezone import now
from victr.models import Event

class EventQuery:

    def all(self):
        """
        Returns ALL events, including invisible ones. Careful...
        """
        return Event.objects.order_by('-close')
    
    def visible(self):
        """
        Returns all events that are visible.
        """
        return Event.objects.filter( 
            Q(scheduled__lte = now()) | Q(scheduled__isnull = True),
            Q(hidden__gte = now()) | Q(hidden__isnull = True),
        ).order_by('-close')
        
    def current(self):
        """
        Returns the current event that project submissions goes to and that the
        front page will display, or returns false if there's no current event.
        """
        try :
            return Event.objects.filter(
                # visible
                Q(scheduled__lte = now()) | Q(scheduled__isnull = True),
                Q(hidden__gte = now()) | Q(hidden__isnull = True),
                # is open or closed less than 48 hours ago
                close__gte = (now() - timedelta(days = 2)),
            #order by close chronologically, not farthest away this time.
            ).order_by('close')[0]
        except IndexError:
            # no events to return, so return False.
            return False