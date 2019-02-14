from django.db import models
import random
import os
from datetime import datetime

from users.models import User

# class Transaction(models.Model):
# 	transaction_id = models.AutoField(primary_key=True)
# 	product_id = models.ForeignKey(Product, unique=True)
# 	timestamp = models.DateTimeField('Date of Transaction', default=datetime.now)

