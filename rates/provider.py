from rates.souces import Fixer, Mock


class RateDataProvider:

    _provider_choices = {'fixer': Fixer(), 'mock': Mock()}

    def __init__(self, imp):
        if imp in self._provider_choices:
            self._imp = self._provider_choices.get(imp)
        else:
            raise ValueError("Invalid type of rate data provider: {}".format(imp))

    def get_rate(self, base=None, symbols=None):
        return self._imp.get_rate_imp(base, symbols)

    def get_historical_rate(self, date):
        return self._imp.get_historical_rate_imp(date)

    def get_rates_between_dates(self, date_from, date_to):
        return self._imp.get_rates_between_dates_imp(date_from, date_to)

    def convert(self, origin, target, amount):
        return self._imp.convert_impl(origin, target, amount)

    def calculate_fluctuaction(self, origin, target, start_date, end_date):
        return self._imp.calculate_fluctuaction(origin, target, start_date, end_date)
