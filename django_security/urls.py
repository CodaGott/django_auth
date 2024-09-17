
from django.contrib import admin
from django.urls import re_path

from django_security import views

urlpatterns = [
    re_path('login/', views.login),
    re_path('signup/', views.sign_up),
    re_path('testToken/', views.test_token),
]
