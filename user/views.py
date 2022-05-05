from django.shortcuts import render, redirect

from FireSale.forms.make_bid_form import MakeBidForm
from FireSale.forms.user_form import UserCreateForm
from user.models import Payment


def index(request):
    return render(request, 'user/index.html')


def place_bid(request):
    if request.method == 'POST':
        form = MakeBidForm(data=request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            user = bid.BuyerID
            bid.PaymentID = user.get_payment_id()
            bid.save()
            return redirect('user-index')
    else:
        form = MakeBidForm()

    return render(request, 'user/place_bid.html', {
        'form': form
    })


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('user-index')
    else:
        form = UserCreateForm()

    return render(request, 'user/create_user.html', {
        'form': form
    })
