# Generated by Django 3.2.25 on 2024-05-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Databases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='relations',
        ),
        migrations.AddField(
            model_name='attribute',
            name='listField',
            field=models.CharField(choices=[('O', 'Oui'), ('N', 'Non')], default='N', max_length=1),
        ),
    ]
