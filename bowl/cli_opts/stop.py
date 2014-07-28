"""
This module is the stop command of bowl.

Created on 14 July 2014
@author: Charlie Lewis
"""
import os
import sys

class stop(object):
    """
    This class is responsible for the stop command of the cli.
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
            try:
                os.kill(int(pid), 9)
                if not args.z:
                    print "The API Server has stopped."
                os.remove(pid_file)
            except OSError, e:
                if not args.z:
                    print >> sys.stderr, "stopping failed: %d (%s)" % (e.errno, e.strerror)
        else:
            if not args.z:
                print "The API Server is not running."
