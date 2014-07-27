from setuptools import setup, find_packages

import fnmatch
import os

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
    version='0.1.1',
    packages=find_packages(),
    license='LICENSE',
    description='Tool for easily building and configuring virtual environments on top of Docker.',
    long_description=open('README.md').read(),
    author=u'Charlie Lewis',
    author_email='charlie.lewis42@gmail.com',
    package_data=files(),
    install_requires=['docker-py==0.3.1', 'requests==2.2.1', 'web.py'],
    entry_points={
        'console_scripts': [
            'bowl = bowl.cli:main',
        ]
    }
)
