from django.contrib import admin
from django.urls import path
from . import views

appname = 'typing_meter'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_entry/', views.new_entry, name = 'new_entry'),
    path('previous_history/', views.previous_history, name = 'previous_history'),
]