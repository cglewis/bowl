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
        # !! TODO this needs to be pull from repositories
        services_dir = os.path.join(args.metadata_path, "services")
        services_dir = os.path.expanduser(services_dir)
        default_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                      "..", "containers/.default"))
        services_dict = {}
        # !! TODO still used for non-json, needs cleanup
        services_dict['databases'] = []
        services_dict['environment'] = []
        services_dict['services'] = []
        services_dict['tools'] = []

        found_services = 0

        # !! TODO note for multiple repositories, need to check if the os/version/service already exists, and provide all options
        # !! TODO should services on remote repositories be able to run on other remote hosts?

        if os.path.exists(services_dir):
            found_services = 1
            try:
                # read oses
                with open(os.path.join(services_dir, "oses"), 'r') as f:
                    oses = f.read()
                os_dict = json.loads(oses)
                services_dict['oses'] = os_dict
                for os_key in os_dict:
                    # read versions for each os
                    with open(os.path.join(services_dir, os_key, "versions"), 'r') as f:
                        versions = f.read()
                    version_dict = json.loads(versions)
                    services_dict['oses'][os_key]['versions'] = version_dict
                    for version_key in version_dict:
                        # read databases for each version
                        with open(os.path.join(services_dir, os_key, version_key, "databases/databases"), 'r') as f:
                            databases = f.read()
                        databases = json.loads(databases)
                        if args.quiet:
                            for database in databases:
                                services_dict['databases'].append(database)
                        elif args.json:
                            services_dict['oses'][os_key]['versions'][version_key]['databases'] = databases
                        else:
                            for database in databases:
                                services_dict['databases'].append(databases[database]['command'])

                        # read environment for each version
                        with open(os.path.join(services_dir, os_key, version_key, "environment/environment"), 'r') as f:
                            environment = f.read()
                        environment = json.loads(environment)
                        if args.quiet:
                            for env in environment:
                                services_dict['environment'].append(env)
                        elif args.json:
                            services_dict['oses'][os_key]['versions'][version_key]['environment'] = environment
                        else:
                            for env in environment:
                                services_dict['environment'].append(environment[env]['command'])

                        # read services for each version
                        with open(os.path.join(services_dir, os_key, version_key, "services/services"), 'r') as f:
                            services = f.read()
                        services = json.loads(services)
                        if args.quiet:
                            for service in services:
                                services_dict['services'].append(service)
                        elif args.json:
                            services_dict['oses'][os_key]['versions'][version_key]['services'] = services
                        else:
                            for service in services:
                                services_dict['services'].append(services[service]['command'])

                        # read tools for each version
                        with open(os.path.join(services_dir, os_key, version_key, "tools/tools"), 'r') as f:
                            tools = f.read()
                        tools = json.loads(tools)
                        if args.quiet:
                            for tool in tools:
                                services_dict['tools'].append(tool)
                        elif args.json:
                            services_dict['oses'][os_key]['versions'][version_key]['tools'] = tools
                        else:
                            for tool in tools:
                                services_dict['tools'].append(tools[tool]['command'])
            except:
                if not args.z:
                    print "failed"

        if os.path.exists(default_dir):
            found_services = 1
            try:
                # read oses
                with open(os.path.join(default_dir, "oses"), 'r') as f:
                    oses = f.read()
                os_dict = json.loads(oses)
                if 'oses' in services_dict:
                    for key in os_dict:
                        # !! TODO do a similar check for versions and services
                        if not key in services_dict['oses']:
                            services_dict['oses'][key] = os_dict[key]
                else:
                    services_dict['oses'] = os_dict
                for os_key in os_dict:
                    # read versions for each os
                    with open(os.path.join(default_dir, os_key, "versions"), 'r') as f:
                        versions = f.read()
                    version_dict = json.loads(versions)
                    services_dict['oses'][os_key]['versions'] = version_dict
                    for version_key in version_dict:
                        # read databases for each version
                        with open(os.path.join(default_dir, os_key, version_key, "databases/databases"), 'r') as f:
                            databases = f.read()
                        databases = json.loads(databases)
                        if args.quiet:
                            for database in databases:
                                services_dict['databases'].append(database)
                        elif args.json:
                            services_dict['oses'][os_key]['versions'][version_key]['databases'] = databases
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
                            services_dict['oses'][os_key]['versions'][version_key]['environment'] = environment
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
                            services_dict['oses'][os_key]['versions'][version_key]['services'] = services
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
                            services_dict['oses'][os_key]['versions'][version_key]['tools'] = tools
                        else:
                            for tool in tools:
                                services_dict['tools'].append(tools[tool]['command'])
            except:
                if not args.z:
                    print "failed"

        if found_services == 0:
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
