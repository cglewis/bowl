"""
This module is the start command of bowl.

Created on 14 July 2014
@author: Charlie Lewis
"""
import os
import sys

import bowl.api

class start(object):
    """
    This class is responsible for the start command of the cli.
    """
    @classmethod
    def check_pid(self, pid):
        """
        Check for the existence of a unix pid.
        """
        try:
            os.kill(int(pid), 0)
        except OSError:
            return False
        else:
            return True

    @classmethod
    def main(self, args):
        running = False
        directory = args.metadata_path
        directory = os.path.expanduser(directory)
        pid_file = os.path.join(directory, "pid")
        if not os.path.exists(directory):
            os.makedirs(directory)

        if os.path.isfile(pid_file):
            with open(pid_file, 'r') as f:
                pid = f.readline()
                running = self.check_pid(pid)

        if running:
            if not args.z:
                print "The API Server is already running."
        else:
            try:
                pid = os.fork()
                if pid > 0:
                    with open(pid_file, 'a') as f:
                        f.write(str(pid))
                    # Exit parent process
                    sys.exit(0)
            except OSError, e:
                if not args.z:
                    print >> sys.stderr, "fork failed: %d (%s)" % (e.errno, e.strerror)
                sys.exit(1)

            # start api server in the background
            bowl.api.main()
