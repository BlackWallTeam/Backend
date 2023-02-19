from django.urls import include, path

app_name = "api"
urlpatterns = [path("search/", include("real_estate_search.search.api.urls"))]
