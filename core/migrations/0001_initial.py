# Generated by Django 4.2.3 on 2023-09-01 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reserva",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cnpj", models.CharField(max_length=100)),
                ("nome_empresa", models.CharField(max_length=100)),
                ("categoria_empresa", models.CharField(max_length=100)),
                ("quitado", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Stand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("localizacao", models.CharField(max_length=100)),
                ("valor", models.FloatField()),
            ],
        ),
    ]