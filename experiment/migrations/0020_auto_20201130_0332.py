# Generated by Django 3.1.3 on 2020-11-30 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0019_auto_20201130_0329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessions',
            old_name='session',
            new_name='session_id',
        ),
    ]
