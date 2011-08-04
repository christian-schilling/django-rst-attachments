#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='django-rst-attachments',
        version='0.0.1',
        description='Attach files to Django models and generate targets for reStructuredText',
        author='Christian Schilling',
        author_email='initcrash@gmail.com',
        url='http://github.com/initcrash/django-rst-attachments/',
        download_url='http://github.com/initcrash/django-rst-attachments/downloads',
            classifiers=[
                "Development Status :: 2 - Pre-Alpha",
                "Framework :: Django",
                "Intended Audience :: Developers",
                "Operating System :: OS Independent",
                "Topic :: Software Development"
            ],
        packages=[
            'attachments',
            'attachments.migrations',
        ],
)
