# Generated by Django 3.2.18 on 2023-02-17 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='link',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='time_minutes',
        ),
    ]
