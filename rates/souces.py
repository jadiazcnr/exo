import abc
from rates.exceptions import ResponseKoException
import requests
import logging

logger = logging.getLogger(__name__)


class Implementor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_rate_imp(self, base, symbols):
        pass

    @abc.abstractmethod
    def get_historical_rate_imp(self, date):
        pass

    @abc.abstractmethod
    def get_rates_between_dates_imp(self, date_from, date_to):
        pass

    @abc.abstractmethod
    def convert_impl(self, origin, target, amount):
        pass

    @abc.abstractmethod
    def calculate_fluctuaction(self, origin, target, start_date, end_date):
        pass


class Fixer(Implementor):
    base_url = "http://data.fixer.io/api/"
    access_key = "9d4707da0c33067ff50c6bd81ae8a494"

    def get_rate_imp(self, base, symbols):
        data = {"access_key": self.access_key}
        if base:
            data["base"] = base
        if symbols:
            data["symbols"] = symbols
            result = requests.get(self.base_url + "latest", data).json()
        return self.__process_response(result)

    def get_historical_rate_imp(self, date):
        data = {"access_key": self.access_key}
        result = requests.get(self.base_url + date.strftime("%Y-%m-%d"), data).json()
        return self.__process_response(result)

    def get_rates_between_dates_imp(self, date_from, date_to):
        data = {
            "access_key": self.access_key,
            "start_date": date_from.strftime("%Y-%m-%d"),
            "end_date": date_to.strftime("%Y-%m-%d")
        }
        result = requests.get(self.base_url + 'timeseries', data).json()
        return self.__process_response(result)

    def convert_impl(self, origin, target, amount):
        data = {
            "access_key": self.access_key,
            "from": origin,
            "to": target,
            "amount": amount
        }
        result = requests.get(self.base_url + "convert", data).json()
        return self.__process_response(result)

    def calculate_fluctuaction(self, origin, target, start_date, end_date):
        data = {
            "access_key": self.access_key,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "base": origin,
            "symbols": target
        }
        result = requests.get(self.base_url + "fluctuation", data).json()
        return self.__process_response(result)

    @staticmethod
    def __process_response(result):
        if result.get("success"):
            return result
        else:
            logging.error(result.get("error"))
            raise ResponseKoException("Error obteniendo los datos")


class Mock(Implementor):

    def get_rate_imp(self):
        return {'success': True, 'timestamp': 1531661887, 'historical': True, 'base': 'EUR', 'date': '2018-07-15',
                'rates': {'AED': 4.293029, 'AFN': 84.347934, 'ALL': 125.66157, 'AMD': 561.855881, 'ANG': 2.15125,
                          'AOA': 297.163981, 'ARS': 31.789443, 'AUD': 1.573814, 'AWG': 2.080645, 'AZN': 1.986553,
                          'BAM': 1.959127, 'BBD': 2.337803, 'BDT': 97.790301, 'BGN': 1.963526, 'BHD': 0.442083,
                          'BIF': 2046.72306, 'BMD': 1.168901, 'BND': 1.580126, 'BOB': 8.019131, 'BRL': 4.500159,
                          'BSD': 1.168901, 'BTC': 0.000184, 'BTN': 80.186638, 'BWP': 11.970608, 'BYN': 2.291512,
                          'BYR': 22910.468667, 'BZD': 2.335236, 'CAD': 1.537812, 'CDF': 1829.919822, 'CHF': 1.170426,
                          'CLF': 0.027668, 'CLP': 759.937914, 'CNY': 7.819839, 'COP': 3338.265572, 'CRC': 659.50592,
                          'CUC': 1.168901, 'CUP': 30.975889, 'CVE': 110.465743, 'CZK': 25.888831, 'DJF': 207.484558,
                          'DKK': 7.454822, 'DOP': 57.779259, 'DZD': 137.532951, 'EGP': 20.853661, 'ERN': 17.522292,
                          'ETB': 31.922698, 'EUR': 1, 'FJD': 2.440788, 'FKP': 0.882759, 'GBP': 0.883187,
                          'GEL': 2.840552, 'GGP': 0.883238, 'GHS': 5.597289, 'GIP': 0.88311, 'GMD': 55.370861,
                          'GNF': 10530.633692, 'GTQ': 8.755661, 'GYD': 242.067799, 'HKD': 9.172416, 'HNL': 27.968352,
                          'HRK': 7.417035, 'HTG': 78.772268, 'HUF': 322.722, 'IDR': 16800.620722, 'ILS': 4.247834,
                          'IMP': 0.883238, 'INR': 80.05689, 'IQD': 1383.979332, 'IRR': 50484.854581, 'ISK': 125.189344,
                          'JEP': 0.883238, 'JMD': 151.665415, 'JOD': 0.828171, 'JPY': 131.302704, 'KES': 117.416148,
                          'KGS': 79.839715, 'KHR': 4730.544629, 'KMF': 493.381614, 'KPW': 1052.011726,
                          'KRW': 1319.109732, 'KWD': 0.353948, 'KYD': 0.958947, 'KZT': 400.301984, 'LAK': 9821.110497,
                          'LBP': 1759.78557, 'LKR': 186.381335, 'LRD': 185.890398, 'LSL': 15.48839, 'LTL': 3.563635,
                          'LVL': 0.725362, 'LYD': 1.60261, 'MAD': 11.063698, 'MDL': 19.444722, 'MGA': 3822.308188,
                          'MKD': 61.344393, 'MMK': 1661.009383, 'MNT': 2861.471185, 'MOP': 9.447534, 'MRO': 414.960423,
                          'MUR': 39.917987, 'MVR': 18.200238, 'MWK': 833.941062, 'MXN': 22.071243, 'MYR': 4.734492,
                          'MZN': 68.252155, 'NAD': 15.491496, 'NGN': 418.467126, 'NIO': 36.563239, 'NOK': 9.479211,
                          'NPR': 128.030248, 'NZD': 1.728576, 'OMR': 0.449798, 'PAB': 1.168901, 'PEN': 3.817052,
                          'PGK': 3.801313, 'PHP': 62.547915, 'PKR': 142.068285, 'PLN': 4.314654, 'PYG': 6667.414342,
                          'QAR': 4.254572, 'RON': 4.643466, 'RSD': 118.01288, 'RUB': 73.093747, 'RWF': 996.383264,
                          'SAR': 4.383619, 'SBD': 9.193765, 'SCR': 15.692547, 'SDG': 20.987864, 'SEK': 10.36255,
                          'SGD': 1.595906, 'SHP': 0.88311, 'SLL': 9584.992389, 'SOS': 666.274229, 'SRD': 8.638615,
                          'STD': 24508.356966, 'SVC': 10.228321, 'SYP': 601.960852, 'SZL': 15.514015, 'THB': 38.912731,
                          'TJS': 11.010472, 'TMT': 3.974265, 'TND': 3.098178, 'TOP': 2.711038, 'TRY': 5.655734,
                          'TTD': 7.893947, 'TWD': 35.726303, 'TZS': 2651.068909, 'UAH': 30.636906, 'UGX': 4374.029665,
                          'USD': 1.168901, 'UYU': 36.633801, 'UZS': 9097.560474, 'VEF': 139917.505463,
                          'VND': 26942.009811, 'VUV': 128.871814, 'WST': 3.038681, 'XAF': 655.566728, 'XAG': 0.073913,
                          'XAU': 0.000942, 'XCD': 3.160249, 'XDR': 0.833745, 'XOF': 655.566728, 'XPF': 119.360706,
                          'YER': 292.050037, 'ZAR': 15.500456, 'ZMK': 10521.520045, 'ZMW': 11.514104,
                          'ZWL': 376.801244}}

    def get_historical_rate_imp(self, date):
        return {'success': True, 'timestamp': 1531661887, 'historical': True, 'base': 'EUR', 'date': '2018-07-15',
                'rates': {'AED': 4.293029, 'AFN': 84.347934, 'ALL': 125.66157, 'AMD': 561.855881, 'ANG': 2.15125,
                          'AOA': 297.163981, 'ARS': 31.789443, 'AUD': 1.573814, 'AWG': 2.080645, 'AZN': 1.986553,
                          'BAM': 1.959127, 'BBD': 2.337803, 'BDT': 97.790301, 'BGN': 1.963526, 'BHD': 0.442083,
                          'BIF': 2046.72306, 'BMD': 1.168901, 'BND': 1.580126, 'BOB': 8.019131, 'BRL': 4.500159,
                          'BSD': 1.168901, 'BTC': 0.000184, 'BTN': 80.186638, 'BWP': 11.970608, 'BYN': 2.291512,
                          'BYR': 22910.468667, 'BZD': 2.335236, 'CAD': 1.537812, 'CDF': 1829.919822, 'CHF': 1.170426,
                          'CLF': 0.027668, 'CLP': 759.937914, 'CNY': 7.819839, 'COP': 3338.265572, 'CRC': 659.50592,
                          'CUC': 1.168901, 'CUP': 30.975889, 'CVE': 110.465743, 'CZK': 25.888831, 'DJF': 207.484558,
                          'DKK': 7.454822, 'DOP': 57.779259, 'DZD': 137.532951, 'EGP': 20.853661, 'ERN': 17.522292,
                          'ETB': 31.922698, 'EUR': 1, 'FJD': 2.440788, 'FKP': 0.882759, 'GBP': 0.883187,
                          'GEL': 2.840552, 'GGP': 0.883238, 'GHS': 5.597289, 'GIP': 0.88311, 'GMD': 55.370861,
                          'GNF': 10530.633692, 'GTQ': 8.755661, 'GYD': 242.067799, 'HKD': 9.172416, 'HNL': 27.968352,
                          'HRK': 7.417035, 'HTG': 78.772268, 'HUF': 322.722, 'IDR': 16800.620722, 'ILS': 4.247834,
                          'IMP': 0.883238, 'INR': 80.05689, 'IQD': 1383.979332, 'IRR': 50484.854581, 'ISK': 125.189344,
                          'JEP': 0.883238, 'JMD': 151.665415, 'JOD': 0.828171, 'JPY': 131.302704, 'KES': 117.416148,
                          'KGS': 79.839715, 'KHR': 4730.544629, 'KMF': 493.381614, 'KPW': 1052.011726,
                          'KRW': 1319.109732, 'KWD': 0.353948, 'KYD': 0.958947, 'KZT': 400.301984, 'LAK': 9821.110497,
                          'LBP': 1759.78557, 'LKR': 186.381335, 'LRD': 185.890398, 'LSL': 15.48839, 'LTL': 3.563635,
                          'LVL': 0.725362, 'LYD': 1.60261, 'MAD': 11.063698, 'MDL': 19.444722, 'MGA': 3822.308188,
                          'MKD': 61.344393, 'MMK': 1661.009383, 'MNT': 2861.471185, 'MOP': 9.447534, 'MRO': 414.960423,
                          'MUR': 39.917987, 'MVR': 18.200238, 'MWK': 833.941062, 'MXN': 22.071243, 'MYR': 4.734492,
                          'MZN': 68.252155, 'NAD': 15.491496, 'NGN': 418.467126, 'NIO': 36.563239, 'NOK': 9.479211,
                          'NPR': 128.030248, 'NZD': 1.728576, 'OMR': 0.449798, 'PAB': 1.168901, 'PEN': 3.817052,
                          'PGK': 3.801313, 'PHP': 62.547915, 'PKR': 142.068285, 'PLN': 4.314654, 'PYG': 6667.414342,
                          'QAR': 4.254572, 'RON': 4.643466, 'RSD': 118.01288, 'RUB': 73.093747, 'RWF': 996.383264,
                          'SAR': 4.383619, 'SBD': 9.193765, 'SCR': 15.692547, 'SDG': 20.987864, 'SEK': 10.36255,
                          'SGD': 1.595906, 'SHP': 0.88311, 'SLL': 9584.992389, 'SOS': 666.274229, 'SRD': 8.638615,
                          'STD': 24508.356966, 'SVC': 10.228321, 'SYP': 601.960852, 'SZL': 15.514015, 'THB': 38.912731,
                          'TJS': 11.010472, 'TMT': 3.974265, 'TND': 3.098178, 'TOP': 2.711038, 'TRY': 5.655734,
                          'TTD': 7.893947, 'TWD': 35.726303, 'TZS': 2651.068909, 'UAH': 30.636906, 'UGX': 4374.029665,
                          'USD': 1.168901, 'UYU': 36.633801, 'UZS': 9097.560474, 'VEF': 139917.505463,
                          'VND': 26942.009811, 'VUV': 128.871814, 'WST': 3.038681, 'XAF': 655.566728, 'XAG': 0.073913,
                          'XAU': 0.000942, 'XCD': 3.160249, 'XDR': 0.833745, 'XOF': 655.566728, 'XPF': 119.360706,
                          'YER': 292.050037, 'ZAR': 15.500456, 'ZMK': 10521.520045, 'ZMW': 11.514104,
                          'ZWL': 376.801244}}

    def convert_impl(self, origin, target, amount):
        return {
            "success": True,
            "query": {
                "from": "GBP",
                "to": "JPY",
                "amount": 25
            },
            "info": {
                "timestamp": 1519328414,
                "rate": 148.972231
            },
            "date": "2018-02-22",
            "result": 3724.305775
        }

    def calculate_fluctuaction(self, origin, target, start_date, end_date):
        return {
            "success": True,
            "fluctuation": True,
            "start_date": "2018-02-25",
            "end_date": "2018-02-26",
            "base": "EUR",
            "rates": {
                "USD": {
                    "start_rate": 1.228952,
                    "end_rate": 1.232735,
                    "change": 0.0038,
                    "change_pct": 0.3078
                }
            }
        }

    def get_rates_between_dates_imp(self, date_from, date_to):
        return {
            "success": True,
            "timeseries": True,
            "start_date": "2012-05-01",
            "end_date": "2012-05-03",
            "base": "EUR",
            "rates": {
                "2012-05-01": {
                    "USD": 1.322891,
                    "AUD": 1.278047,
                    "CAD": 1.302303
                },
                "2012-05-02": {
                    "USD": 1.315066,
                    "AUD": 1.274202,
                    "CAD": 1.299083
                },
                "2012-05-03": {
                    "USD": 1.314491,
                    "AUD": 1.280135,
                    "CAD": 1.296868
                }
            }
        }
