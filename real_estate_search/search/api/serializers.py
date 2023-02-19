from rest_framework import serializers

from real_estate_search.search.models import (
    PrimaryFlat,
    PrimaryFlatPrice,
    SecondaryFlat,
)


class PrimaryFlatPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryFlatPrice
        fields = ["days", "price"]


class PrimaryFlatSerializer(serializers.ModelSerializer):
    prices = PrimaryFlatPriceSerializer(many=True)
    community = serializers.CharField(source="community.name")
    developer = serializers.CharField(source="developer.name")

    class Meta:
        model = PrimaryFlat
        exclude = ["id"]


class SecondaryFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryFlat
        exclude = ["id"]
