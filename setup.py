from setuptools import setup, find_packages
from setuptools.command.install import install

import fnmatch
import os

class MyInstall(install):

    def run(self):
        install.run(self)
        print "Installing man page..."
        os.system('sudo /usr/local/bin/build.sh')

def files():
    base = ['LICENSE', 'README.md', 'requirements.txt']
    matches = []
    for root, dirnames, filenames in os.walk('bowl'):
        for filename in fnmatch.filter(filenames, '*'):
            if not filename.endswith(".py"):
                matches.append(os.path.join(root, filename)[5:])

    data = {}
    data[''] = base
    data['bowl'] = matches
    return data

setup(
    name='bowl',
    version='0.2.0',
    packages=find_packages(),
    license='LICENSE',
    description='Tool for easily building and configuring virtual environments on top of Docker.',
    long_description=open('README.md').read(),
    keywords='bowl docker virtual environment containers services'.split(),
    author=u'Charlie Lewis',
    author_email='charlie.lewis42@gmail.com',
    package_data=files(),
    scripts=['scripts/build.sh'],
    cmdclass={'install': MyInstall},
    install_requires=['docker-py==0.3.1', 'requests==2.2.1', 'web.py'],
    entry_points={
        'console_scripts': [
            'bowl = bowl.cli:main',
        ]
    }
)
