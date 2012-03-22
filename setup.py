#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django_friendlyurls',
    version='0.1.0',
    description='Use friendly urls with Django.',
    author='Jeff Tchang',
    author_email='jeff.tchang@gmail.com',
    url='http://github.com/tachang/django_friendlyurls/',
    zip_safe = False,
    long_description=open('README.rst', 'r').read(),
    packages=[
        'friendlyurls',
    ],
    package_data={
        'friendlyurls': ['templates/friendlyurls/*'],
    },
    requires=[
    ],
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
