# Generated by Django 3.1.3 on 2020-11-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0007_background_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='hand',
            field=models.CharField(choices=[('Oikeakätinen', 'Oikeakätinen'), ('Vasenkätinen', 'Vasenkätinen'), ('Ambidekstri / molempikätinen', 'Ambidekstri / molempikätinen')], default='Mies', max_length=28),
        ),
        migrations.AlterField(
            model_name='background',
            name='sex',
            field=models.CharField(choices=[('Mies', 'Mies'), ('Nainen', 'Nainen'), ('Muu', 'Muu')], max_length=6),
        ),
    ]
