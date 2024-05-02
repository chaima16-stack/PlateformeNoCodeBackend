from django.shortcuts import render
from requests import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from .models import App, Screen, Element
from .serializers import *
from rest_framework.decorators import api_view

class AppListCreateAPIView(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class AppDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class ScreenListCreateAPIView(generics.ListCreateAPIView):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer

class ScreenDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer

class ElementListCreateAPIView(generics.ListCreateAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class ElementDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class ScreensByAppAPIView(generics.ListAPIView):
    serializer_class = ScreenSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Screen.objects.all()
    filterset_class = ScreenFilter

class AppByUserAPIView(generics.ListAPIView):
    serializer_class = AppSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = App.objects.all()
    filterset_class = AppFilter

class ElmentByScreenAPIView(generics.ListAPIView):
    serializer_class = ElementSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Element.objects.all()
    filterset_class = ElementFilter