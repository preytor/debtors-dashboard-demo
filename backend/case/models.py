from django.db import models

from debtors.models import Debtor
from worker.models import Worker

# Create your models here.
class Case(models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    assigned_worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    case_status = models.CharField(max_length=50, choices=[
        ("Open", "Open"),
        ("In progress", "In progress"),
        ("Closed", "Closed"),
    ])

    class Meta:
        db_table = "case"
