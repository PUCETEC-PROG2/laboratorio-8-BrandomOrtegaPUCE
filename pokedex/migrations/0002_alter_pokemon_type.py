# Generated by Django 4.2 on 2024-07-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('F', 'Fuego'), ('A', 'Agua'), ('E', 'Eléctrico'), ('L', 'Lagartija'), ('P', 'Planta')], max_length=30),
        ),
    ]
