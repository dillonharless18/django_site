from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("super-cool-poll", views.super_cool_poll, name="super_cool_poll") # Added to confirm my understanding
]