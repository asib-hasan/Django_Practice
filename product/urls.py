from django.urls import path
from . import views

urlpatterns = [
    path("", views.details, name="product"),
    path("successfully/", views.send),
]