from django.shortcuts import render
from rest_framework import status
from django.conf import settings
from rates.provider import RateDataProvider

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def list(request):
    return Response(_get_provider().get_rate(), status=status.HTTP_200_OK)

@api_view(['GET'])
def convert(request):
    data = request.GET
    data.get("origin")
    data.get("target")
    data.get("amount")


def _get_provider():
    return RateDataProvider(settings.RATE_DATA_PROVIDER)