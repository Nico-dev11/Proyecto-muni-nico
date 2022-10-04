# Generated by Django 4.1 on 2022-08-30 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_caratula_alter_modalidad_violencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='agresor',
            fields=[
                ('dni_agresor', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='casa_de_proteccion',
            fields=[
                ('Casa_de_proteccion', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='expediente',
            fields=[
                ('Nro_expediente', models.IntegerField(max_length=255, primary_key=True, serialize=False)),
                ('DNI_agresor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.agresor')),
            ],
        ),
        migrations.CreateModel(
            name='niño',
            fields=[
                ('dni_niño', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='red_de_contencion',
            fields=[
                ('Red_de_contencion', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='victima',
            fields=[
                ('dni_victima', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('modalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.modalidad')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.caratula')),
            ],
        ),
        migrations.CreateModel(
            name='periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Año', models.DateTimeField()),
                ('Fecha_recepcion', models.DateTimeField()),
                ('Fecha_medida_plazo', models.DateTimeField()),
                ('Nro_expediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.expediente')),
            ],
        ),
        migrations.CreateModel(
            name='medida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medida', models.IntegerField(max_length=100)),
                ('Resolucion', models.CharField(max_length=255)),
                ('Alcance', models.CharField(max_length=255)),
                ('Caratula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.caratula')),
                ('DNI_agresor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.agresor')),
                ('DNI_victima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.victima')),
                ('Nro_expediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.expediente')),
            ],
        ),
        migrations.CreateModel(
            name='localizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Direccion', models.CharField(max_length=255)),
                ('Numero_calle', models.IntegerField(max_length=100)),
                ('Barrio', models.CharField(max_length=255)),
                ('Casa_de_proteccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.casa_de_proteccion')),
                ('DNI_agresor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.agresor')),
                ('DNI_niño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.niño')),
                ('DNI_victima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.victima')),
                ('Red_de_contencion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.red_de_contencion')),
            ],
        ),
        migrations.CreateModel(
            name='informacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=45)),
                ('Apellido', models.CharField(max_length=45)),
                ('Edad', models.IntegerField(max_length=45)),
                ('Fecha_de_nacimiento', models.DateTimeField()),
                ('Trabajo', models.CharField(max_length=45)),
                ('Programa_social', models.CharField(max_length=100)),
                ('Hijos', models.IntegerField(max_length=45)),
                ('Quien_comunica', models.CharField(max_length=100)),
                ('Comentarios', models.CharField(max_length=255)),
                ('Casa_de_proteccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.casa_de_proteccion')),
                ('DNI_agresor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.agresor')),
                ('DNI_niño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.niño')),
                ('DNI_victima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.victima')),
                ('Red_de_contencion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.red_de_contencion')),
            ],
        ),
        migrations.AddField(
            model_name='expediente',
            name='DNI_niño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.niño'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='DNI_victima',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.victima'),
        ),
        migrations.CreateModel(
            name='denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.modalidad')),
                ('Nro_expediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.expediente')),
                ('caratula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.caratula')),
            ],
        ),
    ]
