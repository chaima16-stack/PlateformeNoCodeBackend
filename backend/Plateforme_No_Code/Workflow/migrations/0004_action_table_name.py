# Generated by Django 3.2.25 on 2024-05-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0003_action_champs'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='table_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
