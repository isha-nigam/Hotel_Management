"""reception URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reception, name='reception'),
    path('rlogin', views.rlogin, name='rlogin'),
    path('rhome', views.rhome, name='rhome'),
    path('rlogout', views.rlogout, name='rlogout'),
    path('enter', views.enter, name='enter'),
    path('insert_entry', views.insert_entry, name='insert_entry'),
    path('chk_entries', views.chk_entries, name='chk_entries'),
    path('exit', views.exit, name='exit'),
    path('update_exit', views.update_exit, name='update_exit'),

]
