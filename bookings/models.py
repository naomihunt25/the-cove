from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.booking_date} at {self.booking_time}'