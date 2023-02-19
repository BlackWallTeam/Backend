from django_filters import rest_framework as filters
from rest_framework import generics

from real_estate_search.search.api.serializers import (
    PrimaryFlatSerializer,
    SecondaryFlatSerializer,
)
from real_estate_search.search.models import (
    PrimaryFlat,
    SecondaryFlat,
    Community,
    Developer,
)


class PrimaryFlatFilter(filters.FilterSet):
    max_area = filters.NumberFilter(field_name="area", lookup_expr="lte")
    max_days = filters.NumberFilter(field_name="days_to_be_done", lookup_expr="lte")
    price = filters.RangeFilter(field_name="price")
    community = filters.ChoiceFilter(
        "community__name",
        choices=[
            (x, x)
            for x in Community.objects.all().values_list("name", flat=True).distinct()
        ],
    )
    developer = filters.ChoiceFilter(
        "developer__name",
        choices=[
            (x, x)
            for x in Developer.objects.all().values_list("name", flat=True).distinct()
        ],
    )

    class Meta:
        model = PrimaryFlat
        fields = ["status", "risk"]


class PrimaryFlatList(generics.ListAPIView):
    permission_classes = []
    queryset = PrimaryFlat.objects.all()
    serializer_class = PrimaryFlatSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimaryFlatFilter


class SecondaryFlatFilter(filters.FilterSet):
    max_area = filters.NumberFilter(field_name="area", lookup_expr="lte")
    min_living = filters.NumberFilter(field_name="living_meters", lookup_expr="gte")
    min_kitchen = filters.NumberFilter(field_name="kitchen_meters", lookup_expr="gte")

    floor = filters.RangeFilter(field_name="floor")
    rooms_count = filters.RangeFilter(field_name="rooms_count")
    price = filters.RangeFilter(field_name="price")
    year_of_construction = filters.NumberFilter(
        field_name="year_of_construction", lookup_expr="gte"
    )

    class Meta:
        model = SecondaryFlat
        fields = ["marker"]


class SecondaryFlatList(generics.ListAPIView):
    permission_classes = []
    queryset = SecondaryFlat.objects.all()
    serializer_class = SecondaryFlatSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SecondaryFlatFilter
