# Generated by Django 3.2.18 on 2023-04-21 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listproperty',
            name='is_featured',
        ),
    ]
