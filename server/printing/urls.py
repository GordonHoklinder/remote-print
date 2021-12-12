from django.urls import include, path
from .views import *

urlpatterns = [
    path('print/', submit_gcode, name='print'),
    path('login/', login_request, name='login'),
]
