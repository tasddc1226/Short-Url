import re
from dataclasses import field
from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import Url

User = get_user_model()


class UrlCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["origin_url"]

    def validate_url_format(self, value):
        p = re.compile("^(https?://)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*")
        if not p.match(value):
            return False
        return value
