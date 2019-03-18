from django.db import models
from datetime import datetime
from users.models import User
from products.models import Product


# Create your models here.
class Transaction(models.Model):
    product_name = models.CharField(max_length=120)
    buyer = models.CharField(max_length=20)
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=10)
    date_of_txn = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.id
