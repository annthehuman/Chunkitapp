# Generated by Django 3.1.3 on 2020-12-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0028_auto_20201205_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='jos_opiskelija_tutkintoa',
            field=models.CharField(choices=[('', '---------'), ('Peruskoulutus', 'Peruskoulutus'), ('Ylioppilastutkinto', 'Ylioppilastutkinto'), ('MuuToisenAsteenTutkinto', 'Muu toisen asteen tutkinto'), ('AmkTutkinto', 'Amk-tutkinto'), ('KandidaatinTutkinto', 'Kandidaatin tutkinto'), ('MaisterinTutkinto', 'Maisterin tutkinto'), ('DI', 'DI'), ('TohtorinTutkinto', 'Tohtorin tutkinto')], max_length=26),
        ),
    ]
