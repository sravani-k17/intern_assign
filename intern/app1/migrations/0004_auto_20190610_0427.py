# Generated by Django 2.1.3 on 2019-06-09 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_student_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='fullname',
        ),
    ]
