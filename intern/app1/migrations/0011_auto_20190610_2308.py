# Generated by Django 2.1.2 on 2019-06-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20190610_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.FileField(upload_to='images/'),
        ),
    ]
