# Generated by Django 2.1.2 on 2019-06-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20190610_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.FileField(upload_to='media/images'),
        ),
    ]
