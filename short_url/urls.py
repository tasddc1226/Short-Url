from django.urls import path
from .views import CreateUrlAPIView

urlpatterns = [
    path("create/", CreateUrlAPIView.as_view(), name="create_short_url"),
]
