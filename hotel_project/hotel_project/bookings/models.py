from django.db import models


class Booking(models.Model):
    ROOM_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Deluxe', 'Deluxe'),
        ('Suite', 'Suite'),
    ]

    guest_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES)
    check_in_date = models.DateField()
    no_of_days = models.PositiveIntegerField()

    def __str__(self):
        return self.guest_name
