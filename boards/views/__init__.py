from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from ..models import Board

from .Main import Main
from .Consulting import Consulting