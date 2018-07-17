from django.conf import settings

from rates.provider import RateDataProvider

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.services import calculate_time_weighted_rate, get_rates_between_dates, convert as convert_imp
from api.serializers import RatesSerializer, ConvertSerializer, TimeWeightedSerializer


@api_view(['GET'])
def rates(request):
    """
    Return a list of currencies between two dates
    - date-from -- Start date to get data
    - date-to -- End date to get data
    """

    serializer = RatesSerializer()
    if serializer.validate(request.GET):
        try:
            result = get_rates_between_dates(request.GET.get("date-from"), request.GET.get("date-to"))
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def convert(request):
    """
    Return a conversion of an amount between two currencies
    - origin -- Currency origin [EUR, CHF, USD, GBP]
    - target -- Currency target [EUR, CHF, USD, GBP]
    - amount -- Amount of money
    """
    data = request.GET
    serializer = ConvertSerializer()
    if serializer.validate(data):
        try:
            result = convert_imp(data.get("origin"), data.get("target"), data.get("amount"))
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def time_weighted_rate(request):
    """
    Return a time weighted rate of currency change between a date and today
    - origin -- Currency origin [EUR, CHF, USD, GBP]
    - target -- Currency target [EUR, CHF, USD, GBP]
    - amount -- Amount of money
    - date-invested -- Start date to calculate
    """
    data = request.GET
    serializer = TimeWeightedSerializer()
    if serializer.validate(data):
        try:
            result = calculate_time_weighted_rate(data.get("origin"), data.get("target"), data.get("amount"), data.get("date-invested"))
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(result, status=status.HTTP_200_OK)
