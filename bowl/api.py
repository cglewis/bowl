"""
This module is the web server for running the REST API of bowl.

Created on 14 March 2014
@author: Charlie Lewis
"""

import sys
import web

class main(object):
    """
    This class is responsible for initializing the urls and web server.
    """
    # need __new__ for tests, but fails to call __init__ when actually running
    def __new__(*args, **kw):
        if hasattr(sys, '_called_from_test'):
            print "don't call __init__"
        else: # pragma: no cover
            return object.__new__(*args, **kw)

    def __init__(self, port=8080, host="0.0.0.0"): # pragma: no cover
        urls = self.setup()
        app = web.application(urls, globals())
        web.httpserver.runsimple(app.wsgifunc(), (host, port))

    def setup(self):
        urls = (
            '/', 'root'
        )
        return urls

class root:
    """
    This class is resposible for giving information about the rest server.
    """
    def GET(self):
        """
        GETs the information about the rest server and renders it.

        :return: returns the information
        """
        return ""

if __name__ == "__main__": # pragma: no cover
    main().app.run()
