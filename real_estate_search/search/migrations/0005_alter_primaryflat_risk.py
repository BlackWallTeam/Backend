# Generated by Django 4.1.7 on 2023-02-19 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0004_delete_district_delete_street_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="primaryflat",
            name="risk",
            field=models.CharField(
                choices=[("riskey", "Riskey"), ("good", "Good"), ("bad", "Bad")],
                max_length=20,
            ),
        ),
    ]
