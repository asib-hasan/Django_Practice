from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="paymentone"),
    path("pays/",views.payment_method),
]