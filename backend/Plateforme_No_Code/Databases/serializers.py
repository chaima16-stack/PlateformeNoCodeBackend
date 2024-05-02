from rest_framework import serializers
from .models import Database, Entity, Attribute, Relation

class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = '__all__'
