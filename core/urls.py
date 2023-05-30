from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("costs/", include("costs.urls", namespace="costs")),
    path("account/", include("account.urls", namespace="account")),
]
