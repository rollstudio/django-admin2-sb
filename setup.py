#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
import sys

def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name='django-admin-sb',
    version=0.1,
    description="Theme for django-admin2 based on 'SB Admin'",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='django,djadmin2',
    author="Germano Gabbianelli",
    author_email='tyrion.mx@gmail.com',
    url='http://github.com/tyrion/django-admin2-sb',
    license='MIT',
    packages=get_packages('djadmin2_sb'),
    include_package_data=True,
    install_requires=[
        'django-admin2>=0.5.0',
        ],
    zip_safe=False,
)
