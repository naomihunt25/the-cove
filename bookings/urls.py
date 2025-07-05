from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('bookings/new/', views.booking_form, name='booking_form'),
    path('success/', views.booking_success, name='booking_success'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
]