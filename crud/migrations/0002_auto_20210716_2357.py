# Generated by Django 3.1 on 2021-07-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='dob',
            field=models.CharField(max_length=30),
        ),
    ]