# Generated by Django 2.2.14 on 2020-11-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0002_materia_estudiantes'),
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='materias',
            field=models.ManyToManyField(related_name='materias', to='materias.Materia'),
        ),
    ]
