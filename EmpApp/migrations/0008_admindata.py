# Generated by Django 3.1.1 on 2020-10-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0007_auto_20200930_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]