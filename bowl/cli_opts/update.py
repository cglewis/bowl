"""
This module is the update command of bowl.

Created on 17 July 2014
@author: Charlie Lewis
"""
import os
import requests
import sys

import bowl.api
from bowl.cli_opts import repositories
from bowl.cli_opts import start
from bowl.cli_opts import stop

class update(object):
    """
    This class is responsible for the update command of the cli.
    """
    @classmethod
    def main(self, args):
        # run through hosts in ~/.bowl/repositories
        repos = repositories.repositories.main(args)

        for repo in repos:
            # !! TODO other checks for local running api server
            # if local repo, spin up api server
            if repo == "localhost":
                # start the api server
                path = os.path.dirname(bowl.api.__file__)
                child_pid = os.fork()
                if child_pid == 0:
                    # child process
                    os.chdir(path)
                    start.start.main(args)
                    sys.exit(0)

                with open('services.tar.gz', 'wb') as handle:
                    response = requests.get('http://localhost:8080/repo/services', stream=True)

                    # !! TODO
                    #if not response.ok:
                        # Something went wrong

                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

                pid, status = os.waitpid(child_pid, 0)

                # stop the api server
                stop.stop.main(args)
            else:
                with open('services.tar.gz', 'wb') as handle:
                    response = requests.get('http://'+repo+':8080/repo/services', stream=True)

                    # !! TODO
                    #if not response.ok:
                        # Something went wrong

                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)
