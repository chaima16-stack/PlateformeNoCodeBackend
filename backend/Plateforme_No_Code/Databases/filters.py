import django_filters
from .models import *

class EntityFilter(django_filters.FilterSet):
    class Meta:
        model = Entity
        fields = ['db', 'name_entity']

class AttributeFilter(django_filters.FilterSet):
    class Meta:
        model = Attribute
        fields = ['entity']
