bowl
===
[![Build Status](https://travis-ci.org/cglewis/bowl.png?branch=master)](https://travis-ci.org/cglewis/bowl)
[![Coverage Status](https://coveralls.io/repos/cglewis/bowl/badge.png?branch=master)](https://coveralls.io/r/cglewis/bowl?branch=master) 
[![Docs version](https://readthedocs.org/projects/bowl/badge/?version=latest)](http://bowl.readthedocs.org/en/latest/)
[![PyPI version](https://badge.fury.io/py/bowl.svg)](http://badge.fury.io/py/bowl)
[![downloads](https://pypip.in/d/bowl/badge.png)](https://pypi.python.org/pypi/bowl)

Tool for easily building and configuring virtual environments on top of Docker.

Main features:

- Works with multiple Docker hosts.
- easily add new derives through a simple metadata JSON object and standard Dockerfile.
- Snapshotting containers.
- Spin up the same container on multiple Docker hosts in one go.
- Configure containers at runtime, either in bulk or individually.
- Provides a way to run multiple services on the same container without having to have a Dockerfile for the combined services i.e. Redis Server and SSH.
- Provides a friendly end-user interface for running containers, as well as a straightforward way for operators to manage images, hosts, and available services.
- Services can be easily changed based on environments by changing the path to the metadata for the services.

More information coming soon, including getting started, known issues, roadmap, and more.
