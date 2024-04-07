from django.urls import path
from bheema.views import *

app_name='bheema'

urlpatterns=[
    path('bheema/',bheema,name='bheema'),
    
]