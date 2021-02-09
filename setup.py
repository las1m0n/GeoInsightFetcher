from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='GeoInsightFetcherMadgicx',
    version='1.0',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'task = task.main:main'
        ]
    },
    install_requires=[
        "requests==2.25.1"
    ]
)
