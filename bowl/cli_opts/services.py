"""
This module is the services command of bowl.

Created on 17 July 2014
@author: Charlie Lewis
"""
import json
import os

class services(object):
    """
    This class is responsible for the services command of the cli.
    """
    @classmethod
    def main(self, args):
        services_dir = os.path.join(args.metadata_path, "services")
        services_dir = os.path.expanduser(services_dir)
        default_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "containers/.default"))
        services_dict = {}
        services_dict['databases'] = []
        services_dict['environment'] = []
        services_dict['services'] = []
        services_dict['tools'] = []

        # if services exist, use that, otherwise try to use .default
        if os.path.exists(services_dir):
            # !! TODO
            if not args.z:
                print "services"
        elif os.path.exists(default_dir):
            try:
                # read oses
                with open(os.path.join(default_dir, "oses"), 'r') as f:
                    oses = f.read()
                os_dict = json.loads(oses)
                services_dict['oses'] = os_dict
                for os_key in os_dict:
                    # read versions for each os
                    with open(os.path.join(default_dir, os_key, "versions"), 'r') as f:
                        versions = f.read()
                    version_dict = json.loads(versions)
                    services_dict['versions'] = version_dict
                    for version_key in version_dict:
                        # read databases for each version
                        with open(os.path.join(default_dir, os_key, version_key, "databases/databases"), 'r') as f:
                            databases = f.read()
                        databases = json.loads(databases)
                        if args.quiet:
                            for database in databases:
                                services_dict['databases'].append(database)
                        elif args.json:
                            services_dict['databases'].append(databases)
                        else:
                            for database in databases:
                                services_dict['databases'].append(databases[database]['command'])

                        # read environment for each version
                        with open(os.path.join(default_dir, os_key, version_key, "environment/environment"), 'r') as f:
                            environment = f.read()
                        environment = json.loads(environment)
                        if args.quiet:
                            for env in environment:
                                services_dict['environment'].append(env)
                        elif args.json:
                            services_dict['environment'].append(environment)
                        else:
                            for env in environment:
                                services_dict['environment'].append(environment[env]['command'])

                        # read services for each version
                        with open(os.path.join(default_dir, os_key, version_key, "services/services"), 'r') as f:
                            services = f.read()
                        services = json.loads(services)
                        if args.quiet:
                            for service in services:
                                services_dict['services'].append(service)
                        elif args.json:
                            services_dict['services'].append(services)
                        else:
                            for service in services:
                                services_dict['services'].append(services[service]['command'])

                        # read tools for each version
                        with open(os.path.join(default_dir, os_key, version_key, "tools/tools"), 'r') as f:
                            tools = f.read()
                        tools = json.loads(tools)
                        if args.quiet:
                            for tool in tools:
                                services_dict['tools'].append(tool)
                        elif args.json:
                            services_dict['tools'].append(tools)
                        else:
                            for tool in tools:
                                services_dict['tools'].append(tools[tool]['command'])
            except:
                if not args.z:
                    print "failed"
        else:
            if not args.z:
                print "no services found!"

        if not args.z:
            if args.quiet:
                for key in services_dict:
                    if key != 'oses' and key != 'versions':
                        print key
                        for service in services_dict[key]:
                            print "\t",service
            elif args.json:
                print services_dict
            else:
                for key in services_dict:
                    if key != 'oses' and key != 'versions':
                        for service in services_dict[key]:
                            print service

        return services_dict
