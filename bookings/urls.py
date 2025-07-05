from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('new/', views.booking_create, name='booking_create_view'),
    path('success/', views.booking_success_view, name='booking_success'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
]