import django_filters
from .models import *

class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['element', 'app']
class ActionFilter(django_filters.FilterSet):
    class Meta:
        model =  Action
        fields = ['event']
class ElementActionFilter(django_filters.FilterSet):
    class Meta:
        model =  ElementAction
        fields = ['action','element']