# filters.py
import django_filters
from .models import *

class ScreenFilter(django_filters.FilterSet):
     class Meta:
        model = Screen
        fields = ['app']

class AppFilter(django_filters.FilterSet):
    class Meta:
      model = App
      fields = ['user']

class ElementFilter(django_filters.FilterSet):
    class Meta:
        model = Element
        fields = ['screen']