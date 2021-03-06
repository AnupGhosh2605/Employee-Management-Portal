# Generated by Django 3.1.1 on 2020-09-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0005_auto_20200929_2157'),
    ]

    operations = [
        migrations.DeleteModel(
            name='projectData',
        ),
        migrations.AddField(
            model_name='registerdata',
            name='projectName',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registerdata',
            name='projectPercenatge',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registerdata',
            name='upload',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
