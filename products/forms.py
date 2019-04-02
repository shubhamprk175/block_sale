from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'posted_by', 'price', 'image', 'status', 'posted_on')
