from django.urls import path

from api import views

urlpatterns = [
    path("rates", views.rates, name="rates"),
    path("convert", views.convert, name="convert"),
    path("time-weighted-rate", views.time_weighted_rate, name="time_weighted_rate"),
]