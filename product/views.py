from django.shortcuts import render, get_object_or_404, redirect

from FireSale.forms.product_form import ProductCreateForm
from product.models import Category, Picture
from product.models import Product


# Create your views here.
def index(request):
    # return render(request, 'product/index.html', context={'products': products})
    sort_by = request.GET.get("sort", "l2h")
    if sort_by == "l2h":
        context = {'products': Product.objects.all().order_by('price'),
                   'categories': Category.objects.all().order_by('name')
                   }
    elif sort_by == "h2l":
        context = {'products': Product.objects.all().order_by('-price'),
                   'categories': Category.objects.all().order_by('name')
                   }
    else:
        context = {'products': Product.objects.all().order_by('name'),
                   'categories': Category.objects.all().order_by('name')
                   }
    return render(request, 'product/index.html', context)
  

def home_view(request):
    context = {'categories': Category.objects.all().order_by('name'),
               'products': Product.objects.all().order_by('-CreatedAt')[:4]  # here we can control how many items we get
               }
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
        'form': form
    })


def search_results(request):
    if request.method == 'GET':
        search_term = request.GET.get('search')
        context = {'products': Product.objects.filter(name__icontains=search_term),
                   'categories': Category.objects.all().order_by('name')
                   }
        return render(request, 'product/search_results.html', context)
