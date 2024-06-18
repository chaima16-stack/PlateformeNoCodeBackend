from rest_framework import serializers
from .models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'
class ElementActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementAction
        fields = '__all__'