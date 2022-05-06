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
            user = bid.BuyerID  # Get buyer ID from the Form data
            bid.PaymentID = user.get_payment_id()  # Call get_payment_id function in User class
            bid.save()  # Save all data in database
            return redirect('user-index')
    else:
        product_id = request.GET.get('product_id')  # vista product_id úr GET request-inu
        form = MakeBidForm(initial={'ProductID': product_id})  # Set ProductID á id úr request

    return render(request, 'user/place_bid.html', {
        'form': form
    })
