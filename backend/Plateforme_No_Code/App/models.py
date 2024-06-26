from django.db import models
from enum import Enum
from User.models import User
from Databases.models import Database
class ElementType(Enum):
    BUTTON = 'button'
    INPUT = 'input'
    ICON = 'icon'
    TEXT = 'text'
    LIST = 'list'

class ScreenType(Enum):
    AUTHENTICATION = 'authentification'
    CRUD_PAGE = 'crud page'


class App(models.Model):
    id_app = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='apps', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    database = models.OneToOneField(Database, on_delete=models.CASCADE, null=True)
    date_creation = models.DateField()
    date_update = models.DateField()

class Screen(models.Model):
    id_screen = models.AutoField(primary_key=True)
    app = models.ForeignKey(App, related_name='screens', on_delete=models.CASCADE)
    name_screen = models.CharField(max_length=100)
    type_screen = models.CharField(max_length=100)
    date_creation = models.DateField()
    date_update = models.DateField()

class Element(models.Model):
    id_element = models.CharField(max_length=100,primary_key=True)
    screen = models.ForeignKey(Screen, related_name='elements', on_delete=models.CASCADE)
    type_element = models.CharField(max_length=100)#, choices=[(tag, tag.value) for tag in ElementType])
    label = models.CharField(max_length=100)
    color = models.CharField(max_length=100, null=True)
    textcolor = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100)
    date_creation = models.DateField()
    date_update = models.DateField()