def keyword(key):
    """ 
    change values here to cahnge them sitewide! for example, if you're running
    a hack day, you can change "project" to "hack." Don't worry - Victr
    normalizes capitalization for you.
    """
    key = key.lower()
    keywords = {
        'contender' : 'contender',
        'event' : 'event',
        'events' : 'events',
        'event.rsvp' : 'RSVP',
        'host_name' : 'Victr',
        'project' : 'project',
        'projects' : 'projects',
        'project.title' : 'title',
        'project.description' : 'description',
        'project.url' : 'URL',
        'archive' : 'archive'
    }
    return keywords[key]