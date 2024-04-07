from django.urls import path
from jackie.views import *

app_name='jackie'

urlpatterns=[
    path('jackie/',jackie,name='jackie'),
]