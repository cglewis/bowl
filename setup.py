from setuptools import setup

setup(
    name='punt',
    version='0.1.0',
    packages=['punt', 'punt.cli_opts', ],
    license='LICENSE',
    description='Tool for easily building and configuring virtual environments on top of Docker.',
    long_description=open('README.md').read(),
    author=u'Charlie Lewis',
    author_email='charliel@lab41.org',
    entry_points={
        'console_scripts': [
            'punt = punt.cli:main',
        ]
    }
)
