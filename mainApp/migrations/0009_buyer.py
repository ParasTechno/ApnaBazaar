# Generated by Django 4.0.1 on 2022-03-06 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_product_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(default=0, max_length=15)),
                ('addressline1', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('addressline2', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('addressline3', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('pic', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
            ],
        ),
    ]
