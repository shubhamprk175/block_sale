from django.db import models

# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=50)
	f_name = models.CharField(max_length=50)
	l_name = models.CharField(max_length=50)
	email = models.EmailField(blank=True, unique=True)
	balance = models.DecimalField(decimal_places=2, max_digits=20, default=100)
	# image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

	def __str__(self):
	    return self.user_name
