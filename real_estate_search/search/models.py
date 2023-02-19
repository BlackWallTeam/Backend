import uuid

from django.db import models


class SecondaryFlat(models.Model):
    class MarkerType(models.TextChoices):
        underpriced = "underpriced"
        overpriced = "overpriced"

    link = models.URLField()
    floor = models.IntegerField()
    rooms_count = models.IntegerField()
    area = models.FloatField()
    price = models.IntegerField()
    year_of_construction = models.IntegerField(null=True)
    living_meters = models.FloatField()
    kitchen_meters = models.FloatField()
    pred_price = models.FloatField()
    diff = models.FloatField()
    marker = models.CharField(max_length=20, choices=MarkerType.choices)

    class Meta:
        ordering = ["-marker"]


class Community(models.Model):
    name = models.CharField(unique=True, max_length=50)


class Developer(models.Model):
    name = models.CharField(unique=True, max_length=50)


class PrimaryFlatPrice(models.Model):
    days = models.IntegerField()
    flat = models.ForeignKey(
        "search.PrimaryFlat", related_name="prices", on_delete=models.CASCADE
    )
    price = models.IntegerField()


class PrimaryFlat(models.Model):
    class PrimaryFlatStatus(models.TextChoices):
        short = "short"
        long = "long"

    class PrimaryFlatRisks(models.TextChoices):
        riskey = "riskey"
        good = "good"
        bad = "bad"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=5, choices=PrimaryFlatStatus.choices)
    price = models.IntegerField()
    risk = models.CharField(max_length=20, choices=PrimaryFlatRisks.choices)

    days_to_be_done = models.IntegerField()
    max_price_after_invest = models.IntegerField()
    increase = models.IntegerField()
    increase_procent = models.FloatField()
    days_for_increase = models.IntegerField()

    liter_num = models.CharField(max_length=10, blank=True)
    community = models.ForeignKey(
        Community, null=True, related_name="flats", on_delete=models.SET_NULL
    )
    developer = models.ForeignKey(
        Developer, null=True, related_name="flats", on_delete=models.SET_NULL
    )
    floor = models.CharField(max_length=20)
    area = models.FloatField()
    num_beds = models.IntegerField()
    done_date = models.DateField()

    class Meta:
        ordering = ["increase_procent"]
