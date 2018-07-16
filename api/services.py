from django.conf import settings
from rates.provider import RateDataProvider

from datetime import datetime


def get_rates_between_dates(date_from, date_to):
    return __get_provider().get_rates_between_dates(date_from, date_to)


def convert(origin, target, amount):
    return __get_provider().convert(origin, target, amount)


def calculate_time_weighted_rate(origin, target, amount, date_invested):
    response = __get_provider().calculate_fluctuaction(origin, target, date_invested, datetime.now())
    changing_rate = response.get("rates").get(target).get("change")
    resullt = (changing_rate * float(amount)) + float(amount)
    return {"success": True, "date": datetime.now(), "result": resullt}


def __get_provider():
    return RateDataProvider(settings.RATE_DATA_PROVIDER)