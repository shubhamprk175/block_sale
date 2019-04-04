from django.shortcuts import render, get_object_or_404

from products.models import Product
from users.models import User
from .models import Transaction

# Create your views here.
def confirm(request, product_id):
    print("you bro")
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    context = {
        'product': product
    }
    request.session['product_id'] = product.id
    return render( request, 'transactions/confirm.html', context )

def completed(request):
    if 'product_id' in request.session:
        product_id = request.session['product_id']
        product = get_object_or_404(Product, pk=product_id)
        print(product, "foo")
        if request.user.is_authenticated:
            user_id = request.user.id
        txn = Transaction(product_name=product.product_name, buyer=request.user.username, amount=product.price, seller=product.posted_by)
        txn.save()

        t = Product.objects.get(id=product_id)
        t.status = False
        t.posted_by = request.user
        t.save() # this will update only        

    return render( request, 'transactions/completed.html')
