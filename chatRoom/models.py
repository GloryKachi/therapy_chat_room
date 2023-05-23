from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Therapist(models.Model):
    therapist_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.appointment_date} {self.start_time} {self.end_time} {self.location}'


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_title = models.CharField(max_length=100)
    note_date = models.DateField()
    note_content = models.TextField()
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
