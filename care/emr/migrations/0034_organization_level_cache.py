# Generated by Django 5.1.3 on 2024-12-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0033_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='level_cache',
            field=models.IntegerField(default=0),
        ),
    ]
