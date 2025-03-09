from django.urls import path

from . import views

urlpatterns = [
    path("", views.Spiriter, name="spiriter"),
]