keywords = {
    'archive' : 'archive',
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
    'user' : 'user',
    'users' : 'users',
    'discipline' : 'discipline',
    'disciplines' : 'disciplines',
    'tagline' : 'to the victr go the spoils..'
}

def keyword(key):
    """ 
    change values here to change them sitewide! for example, if you're running
    a hack day, you can change the value for "project" from "project" to "hack." 
    Don't worry - Victr normalizes capitalization for you.
    """
    key_lower = key.lower()
    if key_lower not in keywords:
        return key
    return keywords[key_lower]