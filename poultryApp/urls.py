from django.conf.urls import include, url
from .views import *
app_name = 'poultryApp'

urlpatterns = [
    url(r'^display/$', display, name='display'),
]