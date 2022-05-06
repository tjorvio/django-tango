from django.shortcuts import render, redirect

from FireSale.forms.make_bid_form import MakeBidForm
from user.models import Payment


# Create your views here.
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
        product_id = request.GET.get('product_id')
        form = MakeBidForm(initial={'ProductID': product_id})

    return render(request, 'user/place_bid.html', {
        'form': form
    })
