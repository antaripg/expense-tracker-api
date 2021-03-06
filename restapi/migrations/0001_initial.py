# Generated by Django 3.1.2 on 2021-10-04 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Expense",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField()),
                ("merchant", models.CharField(max_length=255)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("category", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
            ],
        )
    ]
