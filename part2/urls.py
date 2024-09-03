from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.set_prize),
    path('write_csv', views.write_csv)
]
