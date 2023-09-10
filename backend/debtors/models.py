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

    class Meta:
        db_table = "debtor"
