from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from FireSale.forms.make_bid_form import MakeBidForm


# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def place_bid(request):

    if request.method == 'POST':
        form = MakeBidForm(data=request.POST)
        if form.is_valid():
            bid = form.save(commit=False)  # Save data as a bid model class, but don´t commit to database

            bid.save()  # Save all data in database
            return redirect('user-index')
    else:
        product_id = request.GET.get('product_id')  # vista product_id úr GET request-inu
        form = MakeBidForm(initial={'ProductID': product_id})  # Set ProductID á id úr request

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
