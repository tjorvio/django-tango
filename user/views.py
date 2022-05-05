from django.shortcuts import render, get_object_or_404, redirect

from FireSale.forms.user_form import UserCreateForm
from user.models import Country, Payment
from user.models import User

from django.shortcuts import render, redirect

from FireSale.forms.make_bid_form import MakeBidForm
from user.models import Payment



def index(request):
    # return render(request, 'product/index.html', context={'products': products})
    context = {'user': User.objects.all().order_by('name')
               }
    return render(request, 'user/index.html', context)


def create_user(request):



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
    })
