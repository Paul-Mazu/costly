"""Url mappings for the user API"""

from django.urls import path
from .api_views import CreateUserView, CreateTokenView

app_name = "account"

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),
    path("token/", CreateTokenView.as_view(), name="token")
]
