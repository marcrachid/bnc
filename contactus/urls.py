from django.urls import path
from . import views

app_name = 'contactus'

urlpatterns = [
    path('', views.index, name="index"),
]