from django.db import models
<<<<<<< HEAD
from datetime import datetime
from users.models import User
from products.models import Product

||||||| merged common ancestors
=======
from datetime import datetime

from users.models import User
from products.models import Product
>>>>>>> efebcf83e8462e60c65a82f0cf89a18a4aee5fd9

# Create your models here.
<<<<<<< HEAD
class Transaction(models.Model):
	product = models.CharField(Product, max_length=120)
	seller = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	# buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	amount = models.DecimalField(decimal_places=2, max_digits=20, default=10)
	posted_on = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	    return self.product_name
||||||| merged common ancestors
=======
class Transaction(models.Model):
    product_name = models.CharField(max_length=120)
    buyer = models.CharField(max_length=20)
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=10)
    date_of_txn = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.id
>>>>>>> efebcf83e8462e60c65a82f0cf89a18a4aee5fd9
