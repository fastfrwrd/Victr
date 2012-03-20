from django.conf import settings

class Config:

    brand_img = settings.STATIC_URL + 'img/logo.png'

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

    stylesheets = []

    @classmethod
    def brand(self, url=None):
        if isinstance(url, str):
            self.brand_img = settings.STATIC_URL + url
        else:
            return self.brand_img

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


    @classmethod
    def stylesheet(self, arg=None, styles=None):

        # prefix, styles list
        if isinstance(styles, list):
            for style in styles:
                style = settings.STATIC_URL + arg + '/' + style
                if style not in self.stylesheets:
                    self.stylesheets.append(style)

        # style
        elif isinstance(arg, str) and styles is None:
            arg = settings.STATIC_URL + arg;
            self.stylesheets.append(arg)

        # none. just returns list of stylesheets
        elif arg is None and styles is None:
            return self.stylesheets