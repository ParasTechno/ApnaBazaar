# Generated by Django 3.2.7 on 2022-03-04 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_seller_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
