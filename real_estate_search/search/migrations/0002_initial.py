# Generated by Django 4.1.7 on 2023-02-18 23:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("search", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Community",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Developer",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="District",
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
                ("name", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="PrimaryFlat",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("short", "Short"), ("long", "Long")], max_length=5
                    ),
                ),
                ("price", models.IntegerField()),
                (
                    "risk",
                    models.CharField(
                        choices=[
                            ("risk", "Risk"),
                            ("riskey", "Riskey"),
                            ("good", "Good"),
                            ("bad", "Bad"),
                        ],
                        max_length=20,
                    ),
                ),
                ("days_to_be_done", models.IntegerField()),
                ("max_price_after_invest", models.IntegerField()),
                ("increase", models.IntegerField()),
                ("increase_procent", models.FloatField()),
                ("days_for_increase", models.IntegerField()),
                ("liter_num", models.CharField(blank=True, max_length=10)),
                ("floor", models.CharField(max_length=20)),
                ("area", models.FloatField()),
                ("num_beds", models.IntegerField()),
                ("done_date", models.DateField()),
                (
                    "community",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="flats",
                        to="search.community",
                    ),
                ),
                (
                    "developer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="flats",
                        to="search.developer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Street",
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
                ("name", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SecondaryFlat",
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
                ("author", models.IntegerField()),
                ("link", models.URLField()),
                ("floor", models.IntegerField()),
                ("floor_count", models.IntegerField(blank=True)),
                ("rooms_count", models.IntegerField()),
                ("area", models.FloatField()),
                ("price_per_m2", models.IntegerField()),
                ("price", models.IntegerField()),
                ("year_of_construction", models.IntegerField(blank=True, null=True)),
                ("phone", models.CharField(max_length=12)),
                ("residential_complex", models.CharField(blank=True, max_length=30)),
                (
                    "district",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="flats",
                        to="search.district",
                    ),
                ),
                (
                    "street",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="flats",
                        to="search.street",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PrimaryFlatPrice",
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
                ("days", models.IntegerField()),
                ("price", models.IntegerField()),
                (
                    "flat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices",
                        to="search.primaryflat",
                    ),
                ),
            ],
        ),
    ]
