# Generated by Django 4.1.3 on 2022-11-16 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_servicetype_servicetypemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicemodel',
            old_name='service_type',
            new_name='type_id',
        ),
    ]
