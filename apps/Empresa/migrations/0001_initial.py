# Generated by Django 4.1.5 on 2023-01-16 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencia', models.CharField(error_messages={'unique': 'Ya existe un registro con este nombre'}, max_length=50, unique=True, verbose_name='Ingrese nombre de la Dependencia')),
                ('timestamps', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sede', models.CharField(error_messages={'unique': 'Ya existe un registro con este nombre'}, max_length=50, unique=True, verbose_name='Ingrese Nombre de la Sede')),
                ('timestamps', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SedeDependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.dependencia')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.sede')),
            ],
        ),
    ]