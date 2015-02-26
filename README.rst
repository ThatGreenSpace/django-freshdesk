================
Django Freshdesk
================

.. image:: https://secure.travis-ci.org/ThatGreenSpace/django-freshdesk.png?branch=master
   :alt: Build Status
   :scale: 100%
   :target: https://travis-ci.org/ThatGreenSpace/django-freshdesk
.. image:: https://codecov.io/github/ThatGreenSpace/django-freshdesk/coverage.svg?branch=master 
   :alt: Coverage
   :scale: 100%
   :target: https://codecov.io/github/ThatGreenSpace/django-freshdesk?branch=master
.. image:: https://coveralls.io/repos/ThatGreenSpace/django-freshdesk/badge.png?branch=master
   :target: https://coveralls.io/r/ThatGreenSpace/django-freshdesk?branch=master
.. image:: https://badge.fury.io/py/django-freshdesk.png
   :alt: Pypi version
   :scale: 100%
   :target: http://badge.fury.io/py/django-freshdesk
.. image:: https://pypip.in/d/django-freshdesk/badge.png
   :alt: Downloads
   :scale: 100%
   :target: https://crate.io/packages/django-freshdesk?version=latest
.. image:: https://landscape.io/github/ThatGreenSpace/django-freshdesk/master/landscape.png
   :alt: Code health
   :scale: 100%
   :target: https://landscape.io/github/ThatGreenSpace/django-freshdesk/master
.. image:: https://readthedocs.org/projects/django-freshdesk/badge/?version=latest
   :alt: Documentation Status
   :scale: 100%
   :target: https://readthedocs.org/projects/django-freshdesk/

Single Sign-On functionallity between Django and Freshdesk.

The Freshdesk documentation for Single Sign-On is located at
`Freshdesk documentation
<https://support.freshdesk.com/support/articles/31166-single-sign-on-remote-authentication-in>`__

How to use
==========

Get the code
------------

Getting the code for the latest stable release using pip:

::

   $ pip install django-freshdesk

You can also download the source and run:

::

   $ python setup.py install

Add the application to the project settings
-------------------------------------------

Make sure that .django.contrib.auth' is installed and then add register 'freshdesk'
in the 'INSTALLED_APPS' section of your project's settings

::

    INSTALLED_APPS = (
        ...
        'django.contrib.auth',
        'freshdesk',
    )


Setup the settings variables
----------------------------

You must specify two settings variables in your settings module.

* The URL of your support page, will either a subdomain in freshdesk.com
  or your own domain (using a CNAME record)

::

    FRESHDESK_URL = 'http://yourcompany.freshdesk.com/'

* The shared secret you get from Freshdesk when setting up Simple SSO

::

    FRESHDESK_SECRET_KEY = '098f6bcd4621d373cade4e832627b4f6'


Register the urls
-----------------

Add the application urls to your urlconf

::

    urlpatterns = patterns('',
        ...
        url(r'^login/sso/', include('freshdesk.urls')),
    )


Requirements
============

* Python 2.7, 3.2, 3.3 or 3.4
* Django >= 1.6

Bugs and requests
=================

If you have found a bug or or you have a ny request, please use the issue tracker on GitHub.

https://github.com/ThatGreenSpace/django-freshdesk/issues

License
=======

You can use this software under BSD License.
