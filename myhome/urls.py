from django.urls import path
from .views import *

urlpatterns = [
    path("",members, name='members'),
    path("login/",login_user, name='login'),
    path("details/<int:id>/",details,name='login'),
    path("register", register, name='register')
    
]
