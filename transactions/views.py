from django.shortcuts import render, get_object_or_404

from products.models import Product
from users.models import User

# Create your views here.
def confirm(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render( request, 'transactions/confirm.html', context)

def completed(request, product_id):
    
    return render( request, 'transactions/completed.html')
