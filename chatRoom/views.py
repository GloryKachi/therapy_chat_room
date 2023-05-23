from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User, Appointment, Patient
from datetime import datetime


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            error_message = 'invalid login credentials. Please ensure you fill up the appropriate details.'


def book_appointment(request):
    if request.method == 'POST':
        appointment_date = request.POST.get('appointment_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        location = request.POST.get('location')

        patient = request.user

        appointment = Appointment(
            patient=patient,
            appointment_date=datetime.strptime(appointment_date, '%Y-%m-%d').date(),
            start_time=datetime.strptime(start_time, '%H:%M').time(),
            end_time=datetime.strptime(end_time, '%H:%M').time(),
            location=location
        )

        appointment.save()
        return redirect('patient_appointments')
    else:
        return render(request, 'book_appointment_page')



