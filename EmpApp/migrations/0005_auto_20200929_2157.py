# Generated by Django 3.1.1 on 2020-09-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0004_projectdata_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdata',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
