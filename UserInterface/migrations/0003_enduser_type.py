# Generated by Django 5.1.7 on 2025-03-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserInterface', '0002_alter_enduser_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduser',
            name='type',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], default='user', max_length=100),
        ),
    ]
