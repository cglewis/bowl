"""
This module is the services command of bowl.

Created on 17 July 2014
@author: Charlie Lewis
"""
import json
import os

from bowl.cli_opts import repositories

class Object(object):
    pass

class services(object):
    """
    This class is responsible for the services command of the cli.
    """
    @classmethod
    def main(self, args):
        repo_args = Object()
        repo_args.z = True
        repo_args.metadata_path = os.path.expanduser(args.metadata_path)
        repos = repositories.repositories.main(repo_args)

        services_dict = {}
        # !! TODO still used for non-json, needs cleanup
        services_dict['databases'] = []
        services_dict['environment'] = []
        services_dict['services'] = []
        services_dict['tools'] = []

        found_services = 0

        # !! TODO note for multiple repositories, need to check if the os/version/service already exists, and provide all options
        # !! TODO should services on remote repositories be able to run on other remote hosts?

        for repo in repos:
            path = ''
            try:
                path = repo.split(", ")[2]
            except:
                print "unable to parse path from repo", repo
            if path != '' and os.path.exists(path):
                found_services = 1
                try:
                    # read oses
                    with open(os.path.join(path, "oses"), 'r') as f:
                        oses = f.read()
                    os_dict = json.loads(oses)
                    if 'oses' in services_dict:
                        for key in os_dict:
                            if not key in services_dict['oses']:
                                services_dict['oses'][key] = os_dict[key]
                    else:
                        services_dict['oses'] = os_dict
                    for os_key in os_dict:
                        # read versions for each os
                        with open(os.path.join(path, os_key, "versions"), 'r') as f:
                            versions = f.read()
                        version_dict = json.loads(versions)
                        if 'versions' in services_dict['oses'][os_key]:
                            for key in version_dict:
                                if not key in services_dict['oses'][os_key]['versions']:
                                    services_dict['oses'][os_key]['versions'][key] = version_dict[key]
                        else:
                            services_dict['oses'][os_key]['versions'] = version_dict
                        for version_key in version_dict:
                            # !! TODO check if keys already exist
                            # read databases for each version
                            with open(os.path.join(path, os_key, version_key, "databases/databases"), 'r') as f:
                                databases = f.read()
                            databases = json.loads(databases)
                            for database in databases:
                                databases[database]['repository'] = repo.split(", ")[0]
                            if args.quiet:
                                for database in databases:
                                    services_dict['databases'].append(database)
                            elif args.json:
                                services_dict['oses'][os_key]['versions'][version_key]['databases'] = databases
                            else:
                                for database in databases:
                                    services_dict['databases'].append(databases[database]['command'])

                            # read environment for each version
                            with open(os.path.join(path, os_key, version_key, "environment/environment"), 'r') as f:
                                environment = f.read()
                            environment = json.loads(environment)
                            for environ in environment:
                                environment[environ]['repository'] = repo.split(", ")[0]
                            if args.quiet:
                                for env in environment:
                                    services_dict['environment'].append(env)
                            elif args.json:
                                services_dict['oses'][os_key]['versions'][version_key]['environment'] = environment
                            else:
                                for env in environment:
                                    services_dict['environment'].append(environment[env]['command'])

                            # read services for each version
                            with open(os.path.join(path, os_key, version_key, "services/services"), 'r') as f:
                                services = f.read()
                            services = json.loads(services)
                            for service in services:
                                services[service]['repository'] = repo.split(", ")[0]
                            if args.quiet:
                                for service in services:
                                    services_dict['services'].append(service)
                            elif args.json:
                                services_dict['oses'][os_key]['versions'][version_key]['services'] = services
                            else:
                                for service in services:
                                    services_dict['services'].append(services[service]['command'])

                            # read tools for each version
                            with open(os.path.join(path, os_key, version_key, "tools/tools"), 'r') as f:
                                tools = f.read()
                            tools = json.loads(tools)
                            for tool in tools:
                                tools[tool]['repository'] = repo.split(", ")[0]
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
