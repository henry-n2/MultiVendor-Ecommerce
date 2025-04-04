from django.urls import path,include
from . import views

urlpatterns = [
    path('solar/', views.solar_view, name='solar'),
    # path('shop/',include("home.urls")),
]
