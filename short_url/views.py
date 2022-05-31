import uuid
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UrlCreateUpdateSerializer
from .models import Url
from my_settings import HOST, PORT

BASE_URL = f"{HOST}:{PORT}"


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def urls(request):
    urls = Url.objects.all().order_by("-created_at")
    url_list = serializers.serialize("json", urls)
    return HttpResponse(url_list, content_type="text/json-comment-filterd")


class CreateUrlAPIView(APIView):
    """
    Request url : /api/v1/short/create/
    """

    queryset = Url.objects.all()
    serializer_class = UrlCreateUpdateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = UrlCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) and serializer.validate_url_format(
            request.data["origin_url"]
        ):
            short_id = str(uuid.uuid4())[:8]
            short_url = f"{BASE_URL}/api/v1/short/{short_id}"
            serializer.save(
                id=short_id,
                author=request.user,
                origin_url=request.data["origin_url"],
                short_url=short_url,
            )
            return Response(short_url, status=status.HTTP_200_OK)
        else:
            return Response({"errors": "Invalid url format."}, status=status.HTTP_400_BAD_REQUEST)
