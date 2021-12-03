from django.urls import include, path

urlpatterns = [
    path('print/', views.submit_gcode, name='print'),
]
