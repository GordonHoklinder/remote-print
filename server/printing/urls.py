from django.urls import include, path
from .views import *

urlpatterns = [
    path('', show_history, name='history'),
    path('print/', submit_gcode, name='print'),
    path('login/', login_request, name='login'),
]
