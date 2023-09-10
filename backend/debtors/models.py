from django.db import models

# Create your models here.
class Debtor(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    initial_debt = models.DecimalField(max_digits=10, decimal_places=2)
    legal_status = models.CharField(max_length=50, choices=[
        ("Active", "Active"),
        ("In litigation", "In litigation"),
        ("Closed", "Closed"),
    ])

class Payment(models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=[
        ("On time", "On time"),
        ("Late", "Late"),
        ("Missed", "Missed"),
    ])

class Worker(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    role = models.CharField(max_length=50)

class Case(models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    assigned_worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    case_status = models.CharField(max_length=50, choices=[
        ("Open", "Open"),
        ("In progress", "In progress"),
        ("Closed", "Closed"),
    ])
