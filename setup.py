from setuptools import setup

setup(
    name='bowl',
    version='0.1.0',
    packages=['bowl', 'bowl.cli_opts', ],
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
