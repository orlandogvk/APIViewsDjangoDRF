# Generated by Django 2.2.14 on 2020-11-27 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='materias',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='profesores',
        ),
    ]