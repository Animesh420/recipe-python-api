# Generated by Django 3.2.19 on 2023-05-23 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time_minutes',
            new_name='time_in_minutes',
        ),
    ]
