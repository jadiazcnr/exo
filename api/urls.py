from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from api import views

schema_view = get_swagger_view(title='Exo rates API')

urlpatterns = [
    path("rates", views.rates, name="rates"),
    path("convert", views.convert, name="convert"),
    path("time-weighted-rate", views.time_weighted_rate, name="time_weighted_rate"),
]