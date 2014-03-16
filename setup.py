from setuptools import setup

setup(
    name='bowl',
    version='0.1.0',
    packages=['bowl', 'bowl.cli_opts', 'bowl.containers', 'bowl.containers.ubuntu', 'bowl.containers.ubuntu.precise', 'bowl.containers.ubuntu.precise.databases', 'bowl.containers.ubuntu.precise.environment', 'bowl.containers.ubuntu.precise.services'],
    license='LICENSE',
    description='Tool for easily building and configuring virtual environments on top of Docker.',
    long_description=open('README.md').read(),
    author=u'Charlie Lewis',
    author_email='charliel@lab41.org',
    entry_points={
        'console_scripts': [
            'bowl = bowl.cli:main',
        ]
    }
)
