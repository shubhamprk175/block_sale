from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(blank=True, unique=True)
	balance = models.DecimalField(decimal_places=2, max_digits=20, default=100)
	image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)

	def __str__(self):
	    return self.user_name
