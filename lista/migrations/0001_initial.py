# Generated by Django 5.0.2 on 2024-04-19 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produtos",
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
                ("nome", models.CharField(max_length=50)),
                ("quantidade", models.IntegerField(default="")),
                ("preco", models.DecimalField(decimal_places=2, max_digits=6)),
                ("descricao", models.CharField(max_length=255)),
            ],
        ),
    ]
