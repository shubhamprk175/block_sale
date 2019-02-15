from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	user_name = models.CharField(max_length=50) #, default = 'user name')
	first_name = models.CharField(max_length=50)#, default = 'first name')
	last_name = models.CharField(max_length=50)#, default = 'last name')
	password = models.CharField(max_length=256)#, default='password')
	email = models.EmailField(blank=True, unique=True)
	balance = models.DecimalField(decimal_places=2, max_digits=20, default=100)
	image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)

	def __str__(self):
		return self.username
