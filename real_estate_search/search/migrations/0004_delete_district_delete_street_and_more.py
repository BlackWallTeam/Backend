# Generated by Django 4.1.7 on 2023-02-19 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0003_alter_primaryflat_options_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="District",
        ),
        migrations.DeleteModel(
            name="Street",
        ),
        migrations.AlterModelOptions(
            name="secondaryflat",
            options={"ordering": ["-marker"]},
        ),
    ]
