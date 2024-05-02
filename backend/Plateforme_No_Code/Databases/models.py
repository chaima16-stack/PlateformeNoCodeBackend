from django.db import models
required_choices = (
    ('O', 'Oui'),
    ('N', 'Non')
)
TYPE_CHOICES = (
    ('OneToOne', 'OneToOne'),
    ('OneToMany', 'OneToMany'),
    ('ManyToOne', 'ManyToOne'),
    ('ManyToMany', 'ManyToMany'),
)


 
class Database(models.Model):
    name_db = models.CharField(max_length=100)
    date_creation = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

class Entity(models.Model):
    name_entity = models.CharField(max_length=100)
    db = models.ForeignKey(Database, related_name='entities', on_delete=models.CASCADE)
   # relations = models.ManyToManyField('Relation', related_name='entities',null=True)
    date_creation = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
  
class Attribute(models.Model):
    name_attribute = models.CharField(max_length=100)
    type_attribute = models.CharField(max_length=100)
    length = models.IntegerField(null=True)
    listField = models.CharField(max_length=1, choices=required_choices, default='N')
    required = models.CharField(max_length=1, choices=required_choices)
    entity = models.ForeignKey(Entity, related_name='attributes', on_delete=models.CASCADE)
    date_creation = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

class Relation(models.Model):
    name_relation = models.CharField(max_length=100)
    type_relation = models.CharField(max_length=100, choices=TYPE_CHOICES)
    date_creation = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

   