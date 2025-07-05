from django.urls import path
from . import views

urlpatterns = [
# Static 
    path('', views.home, name='home'),               
    path('about/', views.about, name='about'),       
    path('menu/', views.menu, name='menu'),          
    path('contact/', views.contact, name='contact'), 

# Bookings
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/new/', views.booking_form, name='booking_form'),
    path('bookings/success/', views.booking_success, name='booking_success'),
    path('bookings/<int:pk>/', views.booking_detail, name='booking_detail'),
]