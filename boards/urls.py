from django.conf.urls import url
from django.urls import path

from .views import *

app_name = "boards"

urlpatterns = [
    url(r'^$', HomeView.as_view(), name=HomeView.name),
    path('<int:pk>/', HomeDetail.as_view(), name=HomeDetail.name),
    url(r'^consulting01/$', Consulting01.as_view(), name=Consulting01.name),
    url(r'^consulting02/$', Consulting02.as_view(), name=Consulting02.name),
    url(r'^consulting03/$', Consulting03.as_view(), name=Consulting03.name),
]