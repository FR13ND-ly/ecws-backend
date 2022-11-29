from django.urls import path
from . import views

urlpatterns = [
    path('uploadFile/', views.uploadFile),
    path('removeFile/<int:id>/', views.removeFile)
]