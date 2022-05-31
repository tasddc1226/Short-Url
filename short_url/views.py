from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Url


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def urls(request):
    urls = Url.objects.all().order_by("-created_at")
    url_list = serializers.serialize("json", urls)
    return HttpResponse(url_list, content_type="text/json-comment-filterd")
