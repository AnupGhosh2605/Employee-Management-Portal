# Generated by Django 3.1.1 on 2020-09-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('projectName', models.CharField(max_length=100)),
                ('projectPercenatge', models.CharField(max_length=100)),
                ('upload', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
