from django.contrib import admin
from django.urls import path
from django.urls import include
from appfirst import views
urlpatterns = [
    
    path('',views.index,name='index'),
]