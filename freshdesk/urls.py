from django.conf.urls import url
from .views import authenticate

urlpatterns = [
    url(r'^freshdesk/', authenticate)
]
