# Generated by Django 5.0.6 on 2024-07-18 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PageFunctions', '0005_videojuego_juego_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videojuego',
            old_name='juego_slug',
            new_name='slug',
        ),
    ]