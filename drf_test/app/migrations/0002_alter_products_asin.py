# Generated by Django 4.2.11 on 2024-04-19 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='asin',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]