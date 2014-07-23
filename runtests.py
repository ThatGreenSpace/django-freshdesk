#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from os import path as osp

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'freshdesk',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'freshdesk.urls'


def run_tests():
    from django.conf import settings
    settings.configure(
        INSTALLED_APPS = INSTALLED_APPS,
        ROOT_URLCONF = ROOT_URLCONF,
        DATABASES = DATABASES,
        FRESHDESK_URL = "http://example.com/",
        FRESHDESK_SECRET_KEY = "changeme"
    )
    from django_nose import NoseTestSuiteRunner

    test_runner = NoseTestSuiteRunner(verbosity=2)
    failures = test_runner.run_tests(['freshdesk'])
    if failures:
        sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests()
