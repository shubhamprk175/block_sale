from django.db import models
import random
import os
from datetime import datetime

from users.models import User

# Create your models here.
'''
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )
'''
# Create your models here.
class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	product_name = models.CharField(max_length=120)
	posted_by = models.ForeignKey(User, unique=True)
	price = models.DecimalField(decimal_places=2, max_digits=20, default=10)
	# image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	status = models.BooleanField(default=False)
	posted_on = models.DateTimeField('date published', default=datetime.now)
	def __str__(self):
	    return self.product_name


class Transaction(models.Model):
	transaction_id = models.AutoField(primary_key=True)
	product_id = models.ForeignKey(Product, unique=True)
	timestamp = models.DateTimeField('Date of Transaction', default=datetime.now)
