from django.shortcuts import render, get_object_or_404
from product.models import Product
#from django.http import HttpResponse

from product.models import Category
products = [
    {'name': 'Smart Tv',
     'price': 20.0,
     'description': 'An LG smart tv, with remote and power cable',
     'category': 'Electronics'
     },
    {'name': 'Dr. Martin boots',
     'price': 10.0,
     'description': 'Nearly new, no wear and tear. Don´t smell',
     'category': 'Fashion'
     }
]
#categories = [
#    {'id': 1, 'name': 'Art'},
#    {'id': 2, 'name': 'Electronics'},
#    {'id': 3, 'name': 'Entertainment'},
#    {'id': 4, 'name': 'Fashion'},
#    {'id': 5, 'name': 'Furniture'},
#    {'id': 6, 'name': 'Home & Garden'},
#    {'id': 7, 'name': 'Sports'},
#    {'id': 8, 'name': 'Vehicles'},
#]
# Create your views here.


def index(request):
    #return render(request, 'product/index.html', context={'products': products})
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)

def home_view(request):
    context = {'categories': Category.objects.all().order_by('name')}
    return render(request, 'home.html', context)


def get_product_by_id(request, id):
    return render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })