from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class User(AbstractUser):
	REQUIRED_FIELDS = ('first_name','last_name', 'email' )
	balance = models.DecimalField(decimal_places=2, max_digits=20, default=100)
	image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
	def __str__(self):
		return self.username
