# Generated by Django 3.0.8 on 2020-07-16 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200716_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='create',
            new_name='created',
        ),
    ]
