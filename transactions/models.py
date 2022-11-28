from django.db import models
import uuid

# Create your models here.

class Transaction(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    type = models.CharField(
        max_length=1,
    )
    date = models.DateField()
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    ssn = models.CharField(
        max_length=11,
    )
    card = models.CharField(
        max_length=12,
    )
    hour = models.DateTimeField()
    owner = models.CharField(
        max_length=14,
    )
    store = models.CharField(
        max_length=19,
    )