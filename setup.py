#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages
import freshdesk

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    print('git tag -a %s -m "version %s"' % (freshdesk.__version__, freshdesk.__version__))
    print('git push --tags')
    sys.exit()

readme = open('README.rst').read()
changelog = open('CHANGELOG.rst').read().replace('.. :changelog:', '')

setup(
    author='That Green Space Pte Ltd',
    author_email='engineering@thatgreenspace.com.sg',
    name='django-freshdesk',
    version=freshdesk.__version__,
    description='Single Sign-On functionallity between Django and Freshdesk',
    long_description=readme + '\n' + changelog,
    url='https://github.com/ThatGreenSpace/django-freshdesk/',
    license='BSD',
    platforms=['OS Independent'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>1.7,<1.10',
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='runtests'
)
