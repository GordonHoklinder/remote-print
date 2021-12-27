from django.urls import include, path
from .views import *

urlpatterns = [
    path('', submit_gcode, name='print'),
    path('history/', show_history, name='history'),
    path('login/', login_request, name='login'),
]
