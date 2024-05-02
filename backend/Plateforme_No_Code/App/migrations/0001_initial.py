# Generated by Django 3.2.25 on 2024-04-30 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id_app', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_creation', models.DateField()),
                ('date_update', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps', to='User.user')),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id_screen', models.AutoField(primary_key=True, serialize=False)),
                ('name_screen', models.CharField(max_length=100)),
                ('type_screen', models.CharField(max_length=100)),
                ('date_creation', models.DateField()),
                ('date_update', models.DateField()),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='App.app')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id_element', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type_element', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('date_creation', models.DateField()),
                ('date_update', models.DateField()),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='App.screen')),
            ],
        ),
    ]
