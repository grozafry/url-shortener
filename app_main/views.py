from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import re

from app_main import models as Models
from url_shortener.constants import URL_ALLOWED_CHARS_REGEX
from app_main.functions import generate_mapping_url, strip_special_characters
# Create your views here.

@api_view(['POST'])
def create(request):
    data = request.data
    url = data["url"]
    mapping_url = data.get("mapping_url", None)
    if not mapping_url:
        mapping_url = generate_mapping_url(url)
    else:
        mapping_url = strip_special_characters(mapping_url)

    obj = Models.URLMappings(
        url=url,
        mapping_url=mapping_url
    )
    obj.save()

    return Response(mapping_url, status=status.HTTP_200_OK)

@api_view(['GET'])
def redirect(request):
    _path = strip_special_characters(request.path)
    if _path:
        redirect_url = Models.URLMappings.objects.get(
            mapping_url=_path
        ).url
        return Response(status=status.HTTP_301_MOVED_PERMANENTLY, headers={'Location': redirect_url})

    else:
        return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)