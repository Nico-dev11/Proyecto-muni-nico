# Generated by Django 4.1 on 2022-08-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Violencia', models.CharField(choices=[('Domestica', 'Domestica'), ('Institucional', 'Institucional'), ('Laboral', 'Laboral'), ('Reproductiva', 'Reproductiva'), ('Mediatica', 'Mediatica'), ('Callejera', 'Callejera'), ('Obtetrica', 'Obtetrica')], max_length=100)),
            ],
        ),
    ]
