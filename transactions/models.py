from django.db import models
from datetime import datetime
from users.models import User
from products.models import Product


# Create your models here.
class Transaction(models.Model):
	product = models.CharField(Product, max_length=120)
	seller = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	# buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	amount = models.DecimalField(decimal_places=2, max_digits=20, default=10)
	posted_on = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	    return self.product_name
