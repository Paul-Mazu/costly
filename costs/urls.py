from django.urls import path
from .views import listView, detailedListView

app_name = "costs"

urlpatterns = [
    path("<str:requested_year>/", listView, name="months-list"),
    path("<str:requested_year>/<str:requested_month>/", detailedListView, name="detailed-list"),
]
