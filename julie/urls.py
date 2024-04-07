from django.urls import path
from julie.views import *

app_name='julie'

urlpatterns=[
    path('julie/',julie,name='julie'),
]