# Generated by Django 2.1.3 on 2019-06-09 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
