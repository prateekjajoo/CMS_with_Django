# Generated by Django 2.0 on 2019-03-26 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_interiordesignimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='designation',
            new_name='descripsion',
        ),
    ]
