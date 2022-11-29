from django.urls import path, include
from . import views

urlpatterns = [
    path('setPages/', views.setPages), 
    path('getPages/', views.getPages),
]