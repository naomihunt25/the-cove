from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Booking  
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
def home(request):
    return render(request, 'bookings/home.html')

def about(request):
    return render(request, 'bookings/about.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')  
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})


def booking_success(request):
    return render(request, 'bookings/booking_success.html')

@login_required
def booking_list(request):
    if request.user.is_staff:
        bookings = Booking.objects.all().order_by('-booking_date', '-booking_time')
    else:
         bookings = Booking.objects.all().order_by('-booking_date', '-booking_time')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

