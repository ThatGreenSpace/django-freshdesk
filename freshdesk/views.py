from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.utils.encoding import iri_to_uri
from django.utils.http import urlquote
from django.core.exceptions import ImproperlyConfigured

import hashlib
import hmac
import time


@never_cache
@login_required
def authenticate(request):
    if not hasattr(settings, 'FRESHDESK_URL'):
        raise ImproperlyConfigured("Set the FRESHDESK_URL settings variable")
    if not hasattr(settings, 'FRESHDESK_SECRET_KEY'):
        raise ImproperlyConfigured("Set the FRESHDESK_SECRET_KEY settings variable")

    if not request.user:
        raise Http404()

    first_name = request.user.first_name
    last_name = request.user.last_name
    username = request.user.get_username()
    full_name = '{0} {1}'.format(first_name, last_name) if first_name or last_name else username

    utctime = int(time.time())
    data = '{0}{1}{2}{3}'.format(
        full_name, settings.FRESHDESK_SECRET_KEY, request.user.email, utctime)
    generated_hash = hmac.new(
        settings.FRESHDESK_SECRET_KEY.encode(), data.encode(), hashlib.md5).hexdigest()
    url = '{0}login/sso?name={1}&email={2}&timestamp={3}&hash={4}'.format(settings.FRESHDESK_URL,
        urlquote(full_name), urlquote(request.user.email), utctime, generated_hash)
    return HttpResponseRedirect(iri_to_uri(url))
