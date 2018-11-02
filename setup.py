# -*- coding: utf-8 -*-
from setuptools import setup

with open('version') as version_file:
    version = version_file.read()

setup_args = {
    'name': 'chrysopoeia',
    'version': version,
    'description': 'Lightweight functional ETL library for python',
    'url': 'https://github.com/WesselBadenhorst/chrysopoeia',
    'author': 'Wessel Badenhorst',
    'author_email': 'wesselj@gmail.com',
    'license': 'MIT',
    'packages': ['chrysopoeia'],
    'zip_safe': False,
}

setup(**setup_args)
