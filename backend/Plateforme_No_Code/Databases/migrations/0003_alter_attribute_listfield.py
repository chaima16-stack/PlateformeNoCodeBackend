# Generated by Django 3.2.25 on 2024-05-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Databases', '0002_auto_20240501_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='listField',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
