from django.urls import path

from real_estate_search.search.api.views import PrimaryFlatList, SecondaryFlatList

app_name = "search"

urlpatterns = [
    path("primary", PrimaryFlatList.as_view()),
    path("secondary", SecondaryFlatList.as_view()),
]
