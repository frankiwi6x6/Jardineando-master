# Generated by Django 4.2.1 on 2023-06-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[
                    ("A", "Arboles"),
                    ("Ar", "Arbustos"),
                    ("S", "Semillas"),
                    ("H", "Herramientas"),
                ],
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="label",
            field=models.CharField(
                blank=True,
                choices=[("S", "success"), ("D", "danger"), ("W", "warning")],
                max_length=1,
                null=True,
            ),
        ),
    ]
