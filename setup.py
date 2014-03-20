from setuptools import setup, find_packages

setup(
    name='bowl',
    version='0.1.1',
    packages=find_packages(),
    license='LICENSE',
    description='Tool for easily building and configuring virtual environments on top of Docker.',
    long_description=open('README.md').read(),
    author=u'Charlie Lewis',
    author_email='charliel@lab41.org',
    package_data={'': ['LICENSE'], 'bowl': ['containers/*/*/databases/dockerfiles/*/Dockerfile', 'containers/*/*/environment/dockerfiles/*/Dockerfile', 'containers/*/*/services/dockerfiles/*/Dockerfile']},
    entry_points={
        'console_scripts': [
            'bowl = bowl.cli:main',
        ]
    }
)
