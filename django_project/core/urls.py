from django.urls import path
from core.erp.views import MyfirstView, MysecondView

app_name = 'erp'

urlpatterns = [
    path('uno/', MyfirstView, name='Vista1'),
    path('dos/', MysecondView, name='Vista2')
]
