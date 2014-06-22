"""
This module is the web server for running the REST API of bowl.

Created on 14 March 2014
@author: Charlie Lewis
"""

import sys
import web

from bowl.cli_opts import add
from bowl.cli_opts import connect
from bowl.cli_opts import delete
from bowl.cli_opts import disconnect
from bowl.cli_opts import hosts
from bowl.cli_opts import image_import
from bowl.cli_opts import images
from bowl.cli_opts import info
from bowl.cli_opts import kill
from bowl.cli_opts import list
from bowl.cli_opts import login
from bowl.cli_opts import logout
from bowl.cli_opts import logs
from bowl.cli_opts import new
from bowl.cli_opts import remove
from bowl.cli_opts import snapshot
from bowl.cli_opts import version

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
            '/', 'root',
            '/add', 'api_add',
            '/connect/(.*)', 'api_connect',
            '/delete/(.*)', 'api_delete',
            '/disconnect/(.*)', 'api_disconnect',
            '/hosts', 'api_hosts',
            '/images', 'api_images',
            '/import', 'api_image_import',
            '/info', 'api_info',
            '/kill', 'api_kill',
            '/list', 'api_list',
            '/login', 'api_login',
            '/logout', 'api_logout',
            '/logs', 'api_logs',
            '/new', 'api_new',
            '/remove', 'api_remove',
            '/snapshot', 'api_snapshot',
            '/version', 'api_version',
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

class api_add:
    """
    This class is resposible for adding a service
    """
    def POST(self):
        """
        POSTs the new service being added.
        """
        return ""

class api_connect:
    """
    This class is resposible for creating a connection to a docker host.
    """
    def GET(self, host):
        """
        creates a connection to a new docker host.
        """
        class Object(object):
            pass
        args = Object()
        args.DOCKER_HOST = host
        return connect.connect.main(args)

class api_delete:
    """
    This class is resposible for deleting an image.
    """
    def GET(self, image):
        """
        deletes the specified image.
        """
        class Object(object):
            pass
        args = Object()
        args.IMAGE_NAME = image
        return delete.delete.main(args)

class api_disconnect:
    """
    This class is resposible for disconnecting a connection to a docker host.
    """
    def GET(self, host):
        """
        disconnects the specified docker host.
        """
        class Object(object):
            pass
        args = Object()
        args.DOCKER_HOST = host
        return disconnect.disconnect.main(args)

class api_hosts:
    """
    This class is resposible for listing the connected docker hosts.
    """
    def GET(self):
        """
        GETs the connected docker hosts.

        :return: returns the list of connected docker hosts.
        """
        return hosts.hosts.main([])

class api_image_import:
    """
    This class is resposible for importing an image.
    """
    def POST(self):
        """
        POSTs the image being imported.
        """
        return ""

class api_images:
    """
    This class is resposible for listing the images.
    """
    def GET(self):
        """
        GETs the images.

        :return: returns the list of images.
        """
        return images.images.main([])

class api_info:
    """
    This class is resposible for giving system-wide information.
    """
    def GET(self):
        """
        GETs the system-wide information and renders it.

        :return: returns the information.
        """
        return ""

class api_kill:
    """
    This class is resposible for killing a container.
    """
    def POST(self):
        """
        POSTs the container to kill.
        """
        return ""

class api_list:
    """
    This class is resposible for listing the running containers.
    """
    def GET(self):
        """
        GETs the list of running containers.

        :return: returns the list of running containers.
        """
        return ""

class api_login:
    """
    This class is resposible for logging in.
    """
    def POST(self):
        """
        POSTs the user to login.
        """
        return ""

class api_logout:
    """
    This class is resposible for logging out.
    """
    def POST(self):
        """
        POSTs the user to logout.
        """
        return ""

class api_logs:
    """
    This class is resposible for returning logs of a server.
    """
    def GET(self):
        """
        GETs the logs of a server.

        :return: returns the logs of a server.
        """
        return ""

class api_new:
    """
    This class is resposible for creating a new container.
    """
    def POST(self):
        """
        POSTs the creation of a new container.
        """
        return ""

class api_remove:
    """
    This class is resposible for removing a container.
    """
    def POST(self):
        """
        POSTs the removal of a container.
        """
        return ""

class api_snapshot:
    """
    This class is resposible for snapshotting a container.
    """
    def POST(self):
        """
        POSTs the snapshot of a container.
        """
        return ""

class api_version:
    """
    This class is resposible for returning the version of bowl.
    """
    def GET(self):
        """
        GETs the version of bowl.

        :return: returns the version of bowl.
        """
        return version.version.main([])

if __name__ == "__main__": # pragma: no cover
    main().app.run()
