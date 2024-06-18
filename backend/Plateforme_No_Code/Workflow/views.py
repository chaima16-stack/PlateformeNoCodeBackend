from rest_framework import generics, status
from .serializers import * 
from .models import *
from .filters import * 
from django_filters.rest_framework import DjangoFilterBackend

class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ActionListCreate(generics.ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer 

class ElementActionListCreate(generics.ListCreateAPIView):
    queryset = ElementAction.objects.all()
    serializer_class = ElementActionSerializer 

class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ActionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer 

class ElementActionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElementAction.objects.all()
    serializer_class = ElementActionSerializer 

class EventByElementAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Event.objects.all()
    filterset_class = EventFilter

class ActionElementAPIView(generics.ListAPIView):
    serializer_class = ElementActionSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = ElementAction.objects.all()
    filterset_class = ElementActionFilter
    
class ActionByEventAPIView(generics.ListAPIView):
    serializer_class = ActionSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Action.objects.all()
    filterset_class = ActionFilter