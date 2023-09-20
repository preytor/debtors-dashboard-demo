from django.db import models

from case.models import Case

# Create your models here.
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=[
        ("On time", "On time"),
        ("Late", "Late"),
        ("Missed", "Missed"),
    ])

    class Meta:
        db_table = "payment"
