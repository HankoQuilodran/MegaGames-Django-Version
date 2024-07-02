# Generated by Django 5.0.6 on 2024-07-01 22:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PageFunctions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='consola',
            name='consola_nombre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='videojuego',
            name='juego_nombre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='consola',
            name='consola_image',
            field=models.ImageField(default='assets\\img\\CONSOLA_DEFAULT.webp', upload_to='assets\\img'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='juego_image',
            field=models.ImageField(default='assets\\img\\GAME_DEFAULT.png', upload_to='assets\\img'),
        ),
        migrations.CreateModel(
            name='EmpleadoProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empleado_email', models.CharField(max_length=50)),
                ('empleado_direccion', models.CharField(max_length=150)),
                ('empleado_telefono', models.CharField(max_length=15)),
                ('empleado_sueldo', models.PositiveIntegerField()),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('empleado_contrato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PageFunctions.contrato')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_email', models.CharField(max_length=50)),
                ('usuario_direccion', models.CharField(max_length=150)),
                ('usuario_telefono', models.CharField(max_length=15)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
