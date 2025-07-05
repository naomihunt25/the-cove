from django.urls import path
from . import views

urlpatterns = [
# Static 
    path('', views.home, name='home'),               
    path('about/', views.about, name='about'),       
    path('menu/', views.menu, name='menu'),          
    path('contact/', views.contact, name='contact'), 

# Bookings
    path('list/', views.booking_list, name='booking_list'),
    path('bookings/new/', views.booking_form, name='booking_form'),
    path('success/', views.booking_success, name='booking_success'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
]