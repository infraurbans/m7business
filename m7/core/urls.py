from django.urls import path

from m7.core.views import dashboard_view, support_view

app_name = "core"

urlpatterns = [
    path('', dashboard_view, name="dashboard"),
    path('suporte/', support_view, name="support"),

]
