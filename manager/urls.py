"""manager URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.manager, name='manager'),
    path('mlogin', views.mlogin, name='mlogin'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('account', views.account, name='account'),
    path('check', views.check, name='check'),
    path('create_account', views.create_account, name='create_account'),
]
