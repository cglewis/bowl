"""
This module is the test suite of the API for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""
import os
import pkg_resources
import requests
import sys

from bowl import api

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the API.
    """
    def start_server(self):
        path = os.path.dirname(api.__file__)
        child_pid = os.fork()
        pid = -1
        if child_pid == 0:
            # child process
            os.chdir(path)
            api.main()
        else:
            pid = child_pid
        return pid

    def stop_server(self, child_pid):
        if child_pid:
            os.kill(int(child_pid), 9)

    def test_root(self):
        assert 1

    def test_add(self):
        assert 1

    def test_connect(self):
        assert 1

    def test_delete(self):
        assert 1

    def test_disconnect(self):
        assert 1

    def test_hosts(self):
        assert 1

    def test_images(self):
        assert 1

    def test_image_import(self):
        assert 1

    def test_info(self):
        assert 1

    def test_kill(self):
        assert 1

    def test_link(self):
        assert 1

    def test_list(self):
        assert 1

    def test_login(self):
        assert 1

    def test_logout(self):
        assert 1

    def test_logs(self):
        assert 1

    def test_new(self):
        assert 1

    def test_remove(self):
        assert 1

    def test_repositories(self):
        assert 1

    def test_repo_services(self):
        assert 1

    def test_services(self):
        assert 1

    def test_snapshot(self):
        assert 1

    def test_snapshots(self):
        assert 1

    def test_unlink(self):
        assert 1

    def test_uptime(self):
        assert 1

    def test_version(self):
        #child_pid = self.start_server()
        #response = requests.get('http://localhost:8080/version')
        #version = pkg_resources.get_distribution("bowl").version
        #self.stop_server(child_pid)
        #assert response.text == version
        assert 1
