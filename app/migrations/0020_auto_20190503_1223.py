# Generated by Django 2.2.1 on 2019-05-03 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_company_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Company'),
        ),
    ]
