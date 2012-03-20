class Config:

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

    @classmethod
    def keyword(self, arg1, replace=None):
        """ 
        change values here to change them sitewide! for example, if you're running
        a hack day, you can change the value for "project" from "project" to "hack." 
        Don't worry - Victr normalizes capitalization for you.
        """

        # set a whole dictionary of keywords and phrases
        if isinstance(arg1, dict):
            for key, value in arg1.iteritems():
                value = value.lower()
                self.keywords[key] = value
            return

        key_lower = arg1.lower()
        
        # setting a single keyword
        if replace is not None:
            replace = replace.lower()
            self.keywords[arg1] = replace
            return replace

        # getting a keyword
        if key_lower not in self.keywords:
            # keyword not in dict, so return key
            return arg1

        # return the found keyword
        return self.keywords[key_lower]