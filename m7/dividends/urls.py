from django.urls import path

from m7.dividends.views import my_dividends

app_name="dividends"

urlpatterns = [
    path('extratos', my_dividends, name="my_dividends"),
]
