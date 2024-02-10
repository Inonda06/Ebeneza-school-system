from django.urls import path
from .views import admindashboard

app_name='ebenezamanagement'


urlpatterns=[
    path('dashboard/',admindashboard,name='admin'),
]