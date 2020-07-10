from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Main.as_view(), name=Main.name),
    url(r'^consulting/$', Consulting.as_view(), name=Consulting.name),\
]