# Generated by Django 4.1 on 2022-08-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_agresor_casa_de_proteccion_expediente_niño_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='victima',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='agresor',
            name='dni_agresor',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='Nro_expediente',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='Edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='Hijos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='localizacion',
            name='Numero_calle',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='medida',
            name='Medida',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='niño',
            name='dni_niño',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='victima',
            name='dni_victima',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
