from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from FireSale.forms.edit_product_form import ProductEditForm
from FireSale.forms.picture_form import PictureForm
from FireSale.forms.product_form import ProductCreateForm

from product.models import Category, Picture, Product
from user.models import Profile, Bid



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
    product = Product.objects.get(id=id)
    seller_profile = Profile.objects.get(user=product.sellerID)
    same_category = Product.objects.filter(categoryID=product.categoryID).filter(~Q(id=product.id))

    context = {'product': get_object_or_404(Product, pk=id),
               'categories': Category.objects.all().order_by('name'),

               'highest_bid': Bid.objects.filter(ProductID=id).order_by('-BidAmount').first(),

               'seller': seller_profile,

               'similar_products': same_category
               }
    return render(request, 'product/product_details.html', context)


def category_view(request, id):
    context = {'products': Product.objects.filter(categoryID=id),
               'categories': Category.objects.all().order_by('name')
               }
    return render(request, 'product/category.html', context)

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        form2 = PictureForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            product = form.save()
            form2.instance.product = product
            form2.save()
            return redirect('profile')
    else:
        cur_user = request.user
        form = ProductCreateForm(initial={'sellerID': cur_user})
        form2 = PictureForm()

    return render(request, 'product/create_product.html', {
        'form': form,
        'form2': form2
    })


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product_image = Picture.objects.get(product=product)
    if request.method == 'POST':
        form = ProductEditForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            # product_image = Picture(picture=request.POST['picture'], product=product)
            # product_image.save()
            return redirect('profile')
    else:
        # cur_user = request.user
        form = ProductEditForm(instance=product)

    return render(request, 'product/edit_product.html', {
        'form': form,
        'id': id
    })

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('profile')

def search_results(request):
    if request.method == 'GET':
        search_term = request.GET.get('search')
        context = {'products': Product.objects.filter(name__icontains=search_term),
                   'categories': Category.objects.all().order_by('name')
                   }
        return render(request, 'product/search_results.html', context)
