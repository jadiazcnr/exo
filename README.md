
# Exo Currency API

API to get currency information, we need to have a professional Fixer account in order to complete the operations, we can use Mock response to use it

## Installing / Getting started

```shell
git clone https://github.com/jadiazcnr/exo.git
cd exo
python manage.py runserver 8000
```

## Tests
Test Api calls and sources data

```shell
python manage.py test exo
```

# Api Reference
## Rates
GET /rates?date-from=2018-01-01&date-to=2018-02-01

## Convert
GET /convert?origin=EUR&target=USD&amount=20

## Time weighted rate
GET /time-weighted-rate?origin=EUR&target=USD&amount=20&date-invested=2018-01-01

