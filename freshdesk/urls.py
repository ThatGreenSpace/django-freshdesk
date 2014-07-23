from django.conf.urls import patterns, url
from .views import authenticate

urlpatterns = patterns('',
                       url(r'^freshdesk/', authenticate)
                       )
