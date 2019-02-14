from django.db import models
from datetime import datetime

from users.models import User

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=120)
	posted_by = models.ForeignKey(User, unique=True, on_delete=models.DO_NOTHING)
	price = models.DecimalField(decimal_places=2, max_digits=20, default=10)
	image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
	status = models.BooleanField(default=False)
	posted_on = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	    return self.product_name

