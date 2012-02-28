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
        'event.rsvp' : 'RSVP',
        'host_name' : 'Victr',
        'project' : 'project',
        'project.title' : 'title',
        'project.description' : 'description',
        'project.url' : 'URL',
    }
    return keywords[key]