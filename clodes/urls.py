from django.urls import path
from .import views

urlpatterns = [
    path('', views.home ),
    path('clothing/', views.clothing),
    path('checkout/', views.checkout),
    path('contact/', views.contact),
]