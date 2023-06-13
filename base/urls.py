from unicodedata import name
from django.urls import path
from base import views

urlpatterns = [

    path('',views.indexpage,name="indexpage"),
    ]