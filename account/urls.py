from django.urls import path
from .views import UserListAPIView, UserCreateAPIView, UserDetailAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:id>/", UserDetailAPIView.as_view(), name="user_detail"),
]
