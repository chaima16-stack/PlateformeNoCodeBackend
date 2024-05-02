from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics, status
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend

class AttributeListCreate(generics.ListCreateAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

class EntityListCreate(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer 

class RelationListCreate(generics.ListCreateAPIView):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

class DatabaseListCreate(generics.ListCreateAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            
            # Création de l'entité "User"
            user_entity_data = {'name_entity': 'User', 'db': serializer.instance.id}
            user_entity_serializer = EntitySerializer(data=user_entity_data)
            if user_entity_serializer.is_valid():
                user_entity = user_entity_serializer.save()
            else:
                return Response(user_entity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # Création des attributs pour l'entité "User"
            attributes_data = [
                {'name_attribute': 'Password', 'type_attribute': 'String', 'entity': user_entity.id, 'required':'O', 'listField': 'N'},
                {'name_attribute': 'Email', 'type_attribute': 'String', 'entity': user_entity.id, 'required':'O', 'listField': 'N'},
                {'name_attribute': 'Date_creation', 'type_attribute': 'Date', 'entity': user_entity.id, 'required':'O', 'listField': 'N'},
                {'name_attribute': 'Date_update', 'type_attribute': 'Date', 'entity': user_entity.id, 'required':'O', 'listField': 'N'}
            ]
            attribute_serializer = AttributeSerializer(data=attributes_data, many=True)
            if attribute_serializer.is_valid():
                attribute_serializer.save()
            else:
                return Response(attribute_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            headers = self.get_success_headers(serializer.data)
            response_data = serializer.data
            response_data['id'] = serializer.instance.id  # Ajout de l'ID de la base de données dans la réponse
            return Response(response_data['id'], status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AttributeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

class EntityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class RelationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

class DatabaseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer 

class EntitiesByDatabaseAPIView(generics.ListAPIView):
    serializer_class = EntitySerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Entity.objects.all()
    filterset_class = EntityFilter

class AttributeByEntityAPIView(generics.ListAPIView):
    serializer_class = AttributeSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Attribute.objects.all()
    filterset_class = AttributeFilter