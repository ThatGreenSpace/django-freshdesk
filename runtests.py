#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import django

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

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)


def run_tests():
    from django.conf import settings
    settings.configure(
        INSTALLED_APPS=INSTALLED_APPS,
        ROOT_URLCONF=ROOT_URLCONF,
        DATABASES=DATABASES,
        FRESHDESK_URL="http://example.com/",
        FRESHDESK_SECRET_KEY="changeme",
        MIDDLEWARE_CLASSES=MIDDLEWARE_CLASSES,
        TEST_RUNNER='django_nose.NoseTestSuiteRunner'
    )

    if django.VERSION >= (1, 8, 0):
        django.setup()

    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2)
    failures = test_runner.run_tests(['freshdesk'])
    if failures:
        sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests()
