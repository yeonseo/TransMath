from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from ..models import Board


from .HomeView import HomeView
from .HomeView import HomeDetail
from .Consulting import Consulting01
from .Consulting import Consulting02
from .Consulting import Consulting03