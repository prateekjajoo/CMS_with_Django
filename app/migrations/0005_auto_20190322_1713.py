# Generated by Django 2.0 on 2019-03-22 11:43

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_company_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='key',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
