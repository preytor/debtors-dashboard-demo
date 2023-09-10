from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    role = models.CharField(max_length=50)

    class Meta:
        db_table = "worker"
        