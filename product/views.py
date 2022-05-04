from django.shortcuts import render, get_object_or_404, redirect

from FireSale.forms.product_form import ProductCreateForm
from product.models import Category, Picture
from product.models import Product


# Create your views here.
def index(request):
    #return render(request, 'product/index.html', context={'products': products})
    context = {'products': Product.objects.all().order_by('name'),
               'categories': Category.objects.all().order_by('name')
               }
    return render(request, 'product/index.html', context)
  

def home_view(request):
    context = {'categories': Category.objects.all().order_by('name')}
    return render(request, 'home.html', context)


def get_product_by_id(request, id):
    context = {'product': get_object_or_404(Product, pk=id),
               'categories': Category.objects.all().order_by('name')
               }
    return render(request, 'product/product_details.html', context)

def category_view(request, id):
    context = {'products': Product.objects.filter(categoryID=id),
               'categories': Category.objects.all().order_by('name')
               }
    return render(request, 'product/category.html', context)

def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = Picture(picture=request.POST['picture'], product=product)
            product_image.save()
            return redirect('product-index')
    else:
        form = ProductCreateForm()

    return render(request, 'product/create_product.html', {
        'form' : form
    })