from django.urls import path
from . import views

app_name = 'ecotourism'

urlpatterns = [
    path('', views.index, name="index"),
]