from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Static
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path(
        'contact/success/',
        views.contact_success,
        name='contact_success',
    ),

    # Bookings
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/new/', views.booking_form, name='booking_form'),
    path('bookings/success/', views.booking_success, name='booking_success'),
    path('bookings/<int:pk>/', views.booking_detail, name='booking_detail'),
    path(
        'bookings/<int:pk>/edit/',
        views.booking_update,
        name='booking_update',
    ),
    path(
        'bookings/<int:pk>/delete/',
        views.booking_delete,
        name='booking_delete',
    ),

    # Auth
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='bookings/login.html',
        ),
        name='login',
    ),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]
