from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm, UpdateBookingForm


def home(request):
    return render(request, 'bookings/home.html')


def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking added successfully.')
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/add_booking.html', {'form': form})


def booking_list(request):
    bookings = Booking.objects.order_by('check_in_date')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


def booking_detail(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})


def update_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        form = UpdateBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('booking_list')
    else:
        form = UpdateBookingForm(instance=booking)
    return render(request, 'bookings/update_booking.html', {'form': form, 'booking': booking})


def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking cancelled successfully.')
        return redirect('booking_list')
    return render(request, 'bookings/cancel_booking.html', {'booking': booking})
