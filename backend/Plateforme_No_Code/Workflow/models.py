from django.db import models
from App.models import Element, App, Screen

class Event(models.Model):
    type = models.CharField(max_length=100, null=True)
    element = models.ForeignKey(Element,related_name="events", on_delete=models.CASCADE, null=True)
    app = models.ForeignKey(App,related_name="eventsbyapp", on_delete=models.CASCADE, null=True)
    date_creation = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

class Action(models.Model):
    type = models.CharField(max_length=100, null=True)
    event = models.ForeignKey(Event, related_name='actions', on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen,related_name='screensactions', on_delete=models.CASCADE,null=True)
    date_creation = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

class ElementAction(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE, null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, null=True)
    champs = models.CharField(max_length=100,null=True)
    table_name = models.CharField(max_length=100, null=True)
    date_creation = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)