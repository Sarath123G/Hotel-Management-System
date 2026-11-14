from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_name', 'room_type', 'check_in_date', 'no_of_days']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
        }


class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room_type', 'no_of_days']
