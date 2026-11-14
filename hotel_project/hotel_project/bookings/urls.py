from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_booking, name='add_booking'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:id>/', views.booking_detail, name='booking_detail'),
    path('bookings/<int:id>/update/', views.update_booking, name='update_booking'),
    path('bookings/<int:id>/cancel/', views.cancel_booking, name='cancel_booking'),
]
