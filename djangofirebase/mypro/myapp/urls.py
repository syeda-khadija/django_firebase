from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.Contacts, name="con"),
    path("show",views.showData, name="show")
]