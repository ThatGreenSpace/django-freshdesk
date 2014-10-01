#! /usr/bin/env python
# -*- coding: utf8 -*-

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import django.test
from django.conf import settings

from freshdesk import views


class ViewsTestCase(django.test.TestCase):

    def test_user_not_logged_in(self):
        """Test with user not logged in"""
        response = self.client.get(reverse(views.authenticate))
        self.assertEqual(302, response.status_code)
        self.assertEqual(
            response['Location'], r'http://testserver%s?next=/freshdesk/' % settings.LOGIN_URL)

    def test_user_logged_in(self):
        """Test with user logged in"""

        User.objects.create_user('miafey', 'mia.fey@example.com', password='changeme',
                                 first_name='Mia', last_name='Fey')

        self.client.login(username='miafey', password='changeme')
        response = self.client.get(reverse(views.authenticate), follow=False)
        expected_url = 'http://example.com/login/sso?name=Mia%20Fey&email=mia.fey%40example.com'
        self.assertEqual(response.status_code, 302)
        self.assertTrue(expected_url in response.get('Location'))

    def testAnonymous(self):
        """Test a user with no first and last name"""

        User.objects.create_user('phoenixwright', 'phoenix.wright@example.com',
                                 password='changeme')

        self.client.login(username='phoenixwright', password='changeme')
        response = self.client.get(reverse(views.authenticate), follow=False)
        expected_url = 'http://example.com/login/sso?name=phoenixwright&email=phoenix.wright%40example.com'
        self.assertEqual(response.status_code, 302)
        self.assertTrue(expected_url in response.get('Location'))
