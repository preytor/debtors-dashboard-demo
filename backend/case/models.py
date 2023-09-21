from django.db import models

from debtors.models import Debtor
from worker.models import Worker

# Create your models here.
class Case(models.Model):
    id = models.AutoField(primary_key=True)
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    assigned_worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    case_status = models.CharField(max_length=50, choices=[
        ("Open", "Open"),
        ("Closed", "Closed"),
    ])
    borrowed_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_frequency = models.CharField(max_length=50, choices=[
        ("Weekly", "Weekly"),
        ("Bi-weekly", "Bi-weekly"),
        ("Monthly", "Monthly"),
    ], null=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    amortization_period = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "case"
