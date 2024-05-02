from rest_framework import serializers
from .models import App, Screen, Element
from .models import ElementType, ScreenType



class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

class ScreenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Screen
        fields = '__all__'

class ElementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Element
        fields = '__all__'
