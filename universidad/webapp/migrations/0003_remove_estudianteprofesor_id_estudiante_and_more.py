# Generated by Django 4.0.5 on 2022-06-29 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_estudiante_curso_alter_curso_id_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudianteprofesor',
            name='id_Estudiante',
        ),
        migrations.RemoveField(
            model_name='estudianteprofesor',
            name='id_Profesor',
        ),
        migrations.AddField(
            model_name='estudianteprofesor',
            name='Estudiante',
            field=models.ManyToManyField(to='webapp.estudiante'),
        ),
        migrations.AddField(
            model_name='estudianteprofesor',
            name='Profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.profesor'),
        ),
    ]