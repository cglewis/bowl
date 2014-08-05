"""
This module is the web server for running the REST API of bowl.

Created on 14 March 2014
@author: Charlie Lewis
"""
import ast
import datetime
import os
import sys
import tarfile
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
from bowl.cli_opts import link
from bowl.cli_opts import list
from bowl.cli_opts import login
from bowl.cli_opts import logout
from bowl.cli_opts import logs
from bowl.cli_opts import new
from bowl.cli_opts import remove
from bowl.cli_opts import repositories
from bowl.cli_opts import services
from bowl.cli_opts import snapshot
from bowl.cli_opts import snapshots
from bowl.cli_opts import unlink
from bowl.cli_opts import version

START_TIME = datetime.datetime.now()

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
            '/kill/(.*)', 'api_kill',
            '/link/(.*)', 'api_link',
            '/list', 'api_list',
            '/login', 'api_login',
            '/logout', 'api_logout',
            '/logs', 'api_logs',
            '/new', 'api_new',
            '/remove', 'api_remove',
            '/repositories', 'api_repositories',
            '/repo/services', 'api_repo_services',
            '/services', 'api_services',
            '/snapshot/(.*)', 'api_snapshot',
            '/snapshots', 'api_snapshots',
            '/unlink/(.*)', 'api_unlink',
            '/uptime', 'api_uptime',
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
        # !! TODO validate host
        class Object(object):
            pass
        args = Object()
        args.DOCKER_HOST = host
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
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
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return delete.delete.main(args)

class api_disconnect:
    """
    This class is resposible for disconnecting a connection to a docker host.
    """
    def GET(self, host):
        """
        disconnects the specified docker host.
        """
        # !! TODO validate host
        class Object(object):
            pass
        args = Object()
        args.DOCKER_HOST = host
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
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
        class Object(object):
            pass
        args = Object()
        args.z = True
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return hosts.hosts.main(args)

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
        class Object(object):
            pass
        args = Object()
        args.z = True
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return images.images.main(args)

class api_info:
    """
    This class is resposible for giving system-wide information.
    """
    def GET(self):
        """
        GETs the system-wide information and renders it.

        :return: returns the information.
        """
        class Object(object):
            pass
        args = Object()
        args.z = True
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return info.info.main(args)

class api_kill:
    """
    This class is resposible for killing a container.
    """
    def GET(self, container):
        """
        the container to kill.
        """
        class Object(object):
            pass
        args = Object()
        args.CONTAINER = container
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return kill.kill.main(args)

class api_link:
    """
    This class is resposible for linking a service repository host.
    """
    def GET(self, repository):
        """
        creates a link to a new service repository.
        """
        # !! TODO validate repository
        class Object(object):
            pass
        args = Object()
        args.SERVICE_HOST = repository
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return link.link.main(args)

class api_list:
    """
    This class is resposible for listing the running containers.
    """
    def GET(self):
        """
        GETs the list of running containers.

        :return: returns the list of running containers.
        """
        class Object(object):
            pass
        args = Object()
        args.z = True
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return list.list.main(args)

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
    def __init__(self):
        self.data = ""
        self.fullpath = ""
        try:
            self.data = web.data()
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def POST(self):
        """
        POSTs the creation of a new container.
        """
        class Object(object):
            pass
        args = Object()
        args.no_curses = True
        # !! TODO fix me
        args.metadata_path = "~/.bowl"
        try:
            self.data = ast.literal_eval(self.data)
            if "host" in self.data:
                args.host = []
                args.host.append(self.data['host'])
            else:
                return "must specify a host to run the container on"

            if "service" in self.data:
                args.service = []
                args.service.append(self.data['service'])
            else:
                args.service = False
            if "image" in self.data:
                args.image = self.data['image']
            else:
                args.image = False
            if not args.image and not args.service:
                return "must specify a service or image to run"

            if "command" in self.data:
                args.command = self.data['command']
            else:
                args.command = False
            if "entrypoint" in self.data:
                args.entrypoint = self.data['entrypoint']
            else:
                args.entrypoint = False
            if "volume" in self.data:
                args.volume = self.data['volume']
            else:
                args.volume = False
            if "port" in self.data:
                args.port = self.data['port']
            else:
                args.port = False
            if "link" in self.data:
                args.link = self.data['link']
            else:
                args.link = False
            if "name" in self.data:
                args.name = self.data['name']
            else:
                args.name = False
            if "unique" in self.data:
                args.unique = self.data['unique']
            else:
                args.unique = False
            if "user" in self.data:
                args.user = self.data['user']
            else:
                args.user = False

            return new.new.main(args)
        except:
            return "failure"
        return

class api_remove:
    """
    This class is resposible for removing a container.
    """
    def POST(self):
        """
        POSTs the removal of a container.
        """
        return ""

class api_repositories:
    """
    This class is resposible for listing the connected repositories.
    """
    def GET(self):
        """
        GETs the connected repositories.

        :return: returns the list of connected repositories.
        """
        class Object(object):
            pass
        args = Object()
        args.z = True
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return repositories.repositories.main(args)

class api_repo_services:
    """
    This class is resposible for sending services to the client.
    """
    def make_tarfile(self, output_filename, source_dir):
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))

    def GET(self):
        """
        GETs the services and packages them up and serves them up as a static
        file.
        """
        # !! TODO also need to add non-default services
        cwd = os.path.dirname(__file__)
        self.make_tarfile(os.path.join(cwd, "static/default.tar.gz"), os.path.join(cwd, "containers/.default"))
        f = open(os.path.join(cwd, "static/default.tar.gz"), 'r')
        return f.read()

class api_services:
    """
    This class is resposible for listing services.
    """
    def GET(self):
        """
        GETs the list of services.
        """
        class Object(object):
            pass
        args = Object()
        args.z = True
        args.json = True
        args.quiet = False
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return services.services.main(args)

class api_snapshot:
    """
    This class is resposible for snapshotting a container.
    """
    def GET(self, container):
        """
        creates a snapshot of a container.
        """
        class Object(object):
            pass
        args = Object()
        args.CONTAINER = container
        args.z = True
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return snapshot.snapshot.main(args)

class api_snapshots:
    """
    This class is resposible for listing snapshots.
    """
    def GET(self):
        """
        GETs the list of snapshots.
        """
        class Object(object):
            pass
        args = Object()
        args.z = True
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return snapshots.snapshots.main(args)

class api_unlink:
    """
    This class is resposible for unlinking a service repository host.
    """
    def GET(self, repository):
        """
        unlinks the specified service repository.
        """
        # !! TODO validate repository
        class Object(object):
            pass
        args = Object()
        args.SERVICE_HOST = repository
        # !! TODO figure out a way to make this an option
        args.metadata_path = "~/.bowl"
        return unlink.unlink.main(args)

class api_uptime:
    """
    This class is resposible for returning the uptime of the API server.
    """
    def GET(self):
        """
        GETs the uptime of the API server.

        :return: returns the uptime of the API server.
        """
        uptime_seconds = (datetime.datetime.now()-START_TIME).total_seconds()
        uptime_string = str(datetime.timedelta(seconds = uptime_seconds))
        return uptime_string

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
