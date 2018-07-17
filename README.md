
# Exo Currency API

API to get currency information, we need to have a professional Fixer account in order to complete the operations, we can use Mock response to use it menawhile.

Build with Python 3.7, Django 2.0.1 and Djangorestframework 3.7.7

## Installing / Getting started

```shell
sudo apt-get update
sudo apt-get install python3.7

git clone https://github.com/jadiazcnr/exo.git
cd exo

pip install -r requirements.txt
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

