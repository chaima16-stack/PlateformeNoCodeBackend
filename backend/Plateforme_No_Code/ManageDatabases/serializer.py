from rest_framework import serializers


class CreateDatabaseRequestSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    old_db_name = serializers.CharField()

class CreateCollectionSerializer(serializers.Serializer):
    id= serializers.CharField()
    attributes = serializers.DictField(
        child=serializers.CharField(),  # Les clés sont les noms des attributs et les valeurs sont les types
        help_text="Attributs avec leurs types à ajouter à la collection"
    )
    db_name = serializers.CharField()
    collection_name = serializers.CharField()   
    old_collection_name = serializers.CharField() 

class DocumentSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    collection_name = serializers.CharField()
    id = serializers.CharField(required=False)

class AttributesSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    collection_name = serializers.CharField()
    attribute = serializers.CharField()
    old_attribute_name = serializers.CharField(required=False)
  