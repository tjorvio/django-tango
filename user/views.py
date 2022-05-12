from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from FireSale.forms.make_bid_form import MakeBidForm


# Create your views here.
from product.models import Product
from user.forms.profile_form import ProfileForm
from user.models import Profile, Bid, Status


def index(request):
    return render(request, 'user/index.html')

@login_required
def place_bid(request):

    if request.method == 'POST':
        form = MakeBidForm(data=request.POST)
        if form.is_valid():
            bid = form.save(commit=False)  # Save data as a bid model class, but don´t commit to database

            bid.save()  # Save all data in database
            return redirect('profile')
    else:
        product_id = request.GET.get('product_id')  # vista product_id úr GET request-inu
        cur_user = request.user
        print(cur_user)
        print(cur_user.username)
        form = MakeBidForm(initial={'ProductID': product_id, 'UserID':cur_user.id})  # Set ProductID á id úr request

    return render(request, 'user/place_bid.html', {
        'form': form
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })
@login_required
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=profile)
    })
@login_required
def profile(request):
    # all_bids = Bid.objects.all()
    my_products = Product.objects.filter(sellerID=request.user.id)  # .values_list('id')
    open_bids = Bid.objects.filter(ProductID__in=my_products, StatusID=Status.objects.get(id=1))
    my_bids = Bid.objects.filter(UserID=request.user)

    context = {
        'cur_user': request.user,
        'profile_info': Profile.objects.filter(user=request.user).first(),
        'user_products': my_products,
        'open_bids': open_bids,
        'my_bids': my_bids,
               }
    return render(request, 'user/profile.html', context)


@login_required
def accept_bid(request, id):
    bid = get_object_or_404(Bid, pk=id)
    bid.StatusID = Status.objects.get(id=2)
    bid.save()
    product_sold = bid.ProductID
    product_sold.SoldOrNot = 1
    product_sold.save()
    return redirect('profile')


@login_required
def decline_bid(request, id):
    bid = get_object_or_404(Bid, pk=id)
    bid.StatusID = Status.objects.get(id=3)
    bid.save()
    return redirect('profile')


def seller_profile(request, id):
    # Here we are missing review data and rating
    # products =   # .values_list('id')
    seller = Profile.objects.get(id=id).user

    context = {
        'profile_info': Profile.objects.get(id=id),
        'seller_products': Product.objects.filter(sellerID=seller),
               }
    return render(request, 'user/seller_profile.html', context)

@login_required
def check_out(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=profile)
    })
