# Generated by Django 5.1.3 on 2024-12-27 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0044_questionnaire_internal_organization_cache_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicationstatement',
            old_name='dosage',
            new_name='dosage_text',
        ),
    ]
