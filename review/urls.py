from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.django_from,name="registration"),
    path("login/",views.login_form,name="login"),
    path("success/",views.login_success)
]