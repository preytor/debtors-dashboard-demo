from django.db import models

# Create your models here.
class Debtor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    legal_status = models.CharField(max_length=50, choices=[
        ("Active", "Active"),
        ("In litigation", "In litigation"),
        ("Closed", "Closed"),
    ])

    class Meta:
        db_table = "debtor"
