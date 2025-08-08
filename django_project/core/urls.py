from django.urls import path
from core.erp.views import MyfirstView


urlpatterns = [
    path('uno/', MyfirstView),
    path('dos/', MyfirstView)
]
