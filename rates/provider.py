from rates.souces import Fixer, Mock


class RateDataProvider:

    _provider_choices = {'fixer': Fixer(), 'mock': Mock()}

    def __init__(self, imp):
        if imp in self._provider_choices.keys():
            self._imp = self._provider_choices.get(imp)
        else:
            raise ValueError("Invalid type of rate data provider: {}".format(imp))

    def get_rate(self, base = None, symbols = None):
        return self._imp.get_rate_imp(base, symbols)

    def get_historical_rate(self, date):
        return self._imp.get_historical_rate_imp(date)
