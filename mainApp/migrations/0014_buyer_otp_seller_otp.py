# Generated by Django 4.0.1 on 2022-03-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='otp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seller',
            name='otp',
            field=models.IntegerField(default=0),
        ),
    ]
