# Generated by Django 5.1.7 on 2025-03-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserInterface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='budget',
            field=models.IntegerField(default=9000000),
        ),
    ]
