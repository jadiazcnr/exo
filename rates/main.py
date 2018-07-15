from rates.provider import RateDataProvider

provider = RateDataProvider("fixer")
print(provider.get_rate("USD", ["EUR", "AED"]))
