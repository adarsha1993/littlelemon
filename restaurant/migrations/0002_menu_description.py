# Generated by Django 4.1.3 on 2024-10-31 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(default='No description available'),
        ),
    ]
