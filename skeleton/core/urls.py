from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "core"
urlpatterns = [
    path("calcform", views.calc_form, name="calc_form"),
    path("health", views.health),
    path("help", views.help, name="help"),
    path("", views.index, name="index"),
]
