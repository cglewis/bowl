"""
This module is the snapshot command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""
import docker
import os
import uuid

from bowl.cli_opts import list

class Object(object):
    pass

class snapshot(object):
    """
    This class is responsible for the snapshot command of the cli.
    """
    @classmethod
    def main(self, args):
        directory = args.metadata_path
        directory = os.path.expanduser(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        list_args = Object()
        list_args.metadata_path = args.metadata_path
        list_args.z = True
        list_a = list.list.main(list_args)

        commit = str(uuid.uuid4())
        snapshot = {}
        found = 0
        for container in list_a:
            if args.CONTAINER in container:
                 host = container.split(",")[1]
                 cont = container.split(",")[0]
                 commit_name = "bowl-snapshot-"+commit
                 try:
                     c = docker.Client(base_url='tcp://'+host+':2375', version='1.9',
                                       timeout=2)
                     c.commit(cont, repository=commit_name)
                     snapshot[cont] = host+":"+commit_name
                 except:
                     if not args.z:
                         print "unable to connect to "+host
                     return False
                 found = 1

        if found:
            try:
                with open(os.path.join(directory, "snapshots"), 'a') as f:
                    for container in snapshot:
                        f.write("{" +
                                "'container_id': '"+container+"'," +
                                " 'snapshot_id': '"+snapshot[container].split(":")[1]+"'," +
                                " 'host': '"+snapshot[container].split(":")[0]+"'" +
                                "}\n")
                        if not args.z:
                            print "snapshotted",
                            print container + " on",
                            print snapshot[container].split(":")[0],
                            print "to repository;",
                            print snapshot[container].split(":")[1]
            except:
                if not args.z:
                    print "unable to snapshot container"
                return False
        else:
            if not args.z:
                print args.CONTAINER, "is not a running container"
            return False
        return True
