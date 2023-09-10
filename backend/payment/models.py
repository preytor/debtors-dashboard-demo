from django.db import models

from debtors.models import Debtor

# Create your models here.
class Payment(models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=[
        ("On time", "On time"),
        ("Late", "Late"),
        ("Missed", "Missed"),
    ])

    class Meta:
        db_table = "payment"
