from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Url(models.Model):
    id = models.CharField(
        max_length=8,
        primary_key=True,
        unique=True,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    origin_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=100)
    hits = models.PositiveIntegerField(default=0)
    in_use = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "url"
        indexes = [models.Index(fields=["id"])]
