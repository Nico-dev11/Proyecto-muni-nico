# Generated by Django 4.1 on 2022-08-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victima',
            name='DNI_victima',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='victima',
            name='Id_caratula',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='victima',
            name='Id_modalidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='victima',
            name='Id_tipo',
            field=models.IntegerField(default=0),
        ),
    ]