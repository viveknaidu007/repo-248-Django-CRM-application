# Generated by Django 4.2.3 on 2025-03-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("name", models.CharField(max_length=100)),
                ("subject", models.CharField(max_length=100)),
                ("contact", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="teachers/"),
                ),
            ],
        ),
    ]
