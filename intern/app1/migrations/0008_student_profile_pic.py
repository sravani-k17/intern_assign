# Generated by Django 2.1.3 on 2019-06-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_student_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(default='images/d1.jpg', upload_to='images'),
        ),
    ]
