# Generated by Django 4.0.5 on 2022-06-30 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_estudianteprofesor_id_estudiante_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('numero_calle', models.IntegerField(max_length=5)),
            ],
        ),
    ]