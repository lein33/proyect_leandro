# Generated by Django 4.1.3 on 2022-12-02 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "dni",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=8)),
                ("edad", models.IntegerField(blank=True)),
                ("sexo", models.CharField(max_length=10)),
                ("correo", models.CharField(max_length=25)),
                ("pais", models.CharField(max_length=15)),
                ("provincia", models.CharField(max_length=15)),
                ("direccion", models.CharField(max_length=25)),
                ("cod_postal", models.CharField(max_length=15)),
                ("celular", models.CharField(max_length=15)),
            ],
        ),
    ]
