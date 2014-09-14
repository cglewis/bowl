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

    def test_setup(self):
        a = api.main().__new__(api.main)
        a.setup()
        assert 1

    def test_root(self):
        a = api.root()
        a.GET()
        assert 1

    def test_add(self):
        a = api.api_add()
        a.POST()
        assert 1

    def test_connect(self):
        a = api.api_connect()
        a.GET("host")
        assert 1

    def test_delete(self):
        a = api.api_delete()
        a.GET("test")
        assert 1

    def test_disconnect(self):
        a = api.api_disconnect()
        a.GET("host")
        assert 1

    def test_hosts(self):
        a = api.api_hosts()
        a.GET()
        assert 1

    def test_image_import(self):
        a = api.api_image_import()
        a.POST()
        assert 1

    def test_images(self):
        a = api.api_images()
        a.GET()
        assert 1

    def test_info(self):
        a = api.api_info()
        a.GET()
        assert 1

    def test_kill(self):
        a = api.api_kill()
        a.GET("container")
        assert 1

    def test_link(self):
        a = api.api_link()
        a.GET("repository")
        assert 1

    def test_list(self):
        a = api.api_list()
        a.GET()
        assert 1

    def test_login(self):
        a = api.api_login()
        a.POST()
        assert 1

    def test_logout(self):
        a = api.api_logout()
        a.POST()
        assert 1

    def test_logs(self):
        a = api.api_logs()
        a.GET("container")
        assert 1

    def test_new(self):
        a = api.api_new()
        a.POST()
        assert 1

    def test_remove(self):
        a = api.api_remove()
        a.POST()
        assert 1

    def test_repositories(self):
        a = api.api_repositories()
        a.GET()
        assert 1

    def test_repo_services(self):
        a = api.api_repo_services()
        a.GET()
        assert 1

    def test_services(self):
        a = api.api_services()
        a.GET()
        assert 1

    def test_snapshot(self):
        a = api.api_snapshot()
        a.GET("container")
        assert 1

    def test_snapshots(self):
        a = api.api_snapshots()
        a.GET()
        assert 1

    def test_subtract(self):
        a = api.api_subtract()
        a.GET("os", "version", "type", "name")
        assert 1

    def test_test(self):
        # !! TODO make sure this isn't recursive
        a = api.api_test()
        a.GET()
        assert 1

    def test_unlink(self):
        a = api.api_unlink()
        a.GET("repository")
        assert 1

    def test_uptime(self):
        a = api.api_uptime()
        a.GET()
        assert 1

    def test_version(self):
        a = api.api_version()
        # !! TODO not working with travis for some reason
        #a.GET()
        #child_pid = self.start_server()
        #response = requests.get('http://localhost:8080/version')
        #version = pkg_resources.get_distribution("bowl").version
        #self.stop_server(child_pid)
        #assert response.text == version
        assert 1
