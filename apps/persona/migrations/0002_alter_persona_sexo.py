# Generated by Django 4.1.3 on 2022-12-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("persona", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="persona",
            name="sexo",
            field=models.CharField(
                choices=[("Femenino", "Femenino"), ("Masculino", "Masculino")],
                default="F",
                max_length=10,
            ),
        ),
    ]
