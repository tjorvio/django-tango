from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from FireSale.forms.register_form import SignUpForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from formtools.wizard.views import NamedUrlSessionWizardView

import user
from FireSale.forms.make_bid_form import MakeBidForm

# Create your views here.
from product.models import Product
from user.forms.checkout_address_form import CheckOutAddressForm
from user.forms.checkout_cc_form import CheckOutCCForm
from user.forms.checkout_confirm_form import CheckOutConfirmForm
from user.forms.profile_form import ProfileForm
from user.models import Profile, Bid, Status, BillingAddress, PaymentInfo, Order


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
        form = MakeBidForm(initial={'ProductID': product_id, 'UserID': cur_user.id})  # Set ProductID á id úr request
    context = {
        'form': form,
    }
    if request.user.is_authenticated:
        context['profile_info'] = Profile.objects.filter(user=request.user).first()
    return render(request, 'user/place_bid.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'user/register.html', {
        'form': form
    })


@login_required
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    context = {
        'form': ProfileForm(instance=profile)
    }
    if request.user.is_authenticated:
        context['profile_info'] = Profile.objects.filter(user=request.user).first()
    return render(request, 'user/edit_profile.html', context)


@login_required
def profile(request):
    # all_bids = Bid.objects.all()
    my_products = Product.objects.filter(sellerID=request.user.id)  # .values_list('id')
    open_bids = Bid.objects.filter(ProductID__in=my_products, StatusID=Status.objects.get(id=1))
    my_bids = Bid.objects.filter(UserID=request.user).filter(~Q(StatusID=Status.objects.get(id=4)))
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


def delete_bid(request, id):
    bid = get_object_or_404(Bid, pk=id)
    bid.delete()
    return redirect('profile')


def seller_profile(request, id):
    # Here we are missing review data and rating
    # products =   # .values_list('id')
    seller = Profile.objects.get(id=id).user

    context = {
        'seller_info': Profile.objects.get(id=id),
        'seller_products': Product.objects.filter(sellerID=seller),
    }
    if request.user.is_authenticated:
        context['profile_info'] = Profile.objects.filter(user=request.user).first()
    return render(request, 'user/seller_profile.html', context)


# @login_required
# def check_out(request, id):
#     profile = Profile.objects.filter(user=request.user).first()
#     if request.method == 'POST':
#         form = ProfileForm(instance=profile, data=request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile')
#     return render(request, 'user/edit_profile.html', {
#         'form': ProfileForm(instance=profile)
#     })


FORMS = [
    ("address", user.forms.checkout_address_form),
    ("cc", user.forms.checkout_cc_form),
    # ("confirmation", user.forms.checkout_confirm_form)
]

TEMPLATES = {
    'address': 'user/checkout/billing_address.html',
    'cc': 'user/checkout/creditcard.html',
    # 'confirmation': 'user/checkout/confirm_order.html',

}


class OrderWizard(NamedUrlSessionWizardView):

    def get_form_instance(self, step):
        if step == 'cc':
            bid_id = Bid.objects.get(id=self.request.session['bid'])
            pay_instance = PaymentInfo(bid=bid_id)
            return pay_instance
        else:
            return None

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        buyer = self.request.user
        buyer_pro = Profile.objects.get(user=buyer)
        bid_id = self.request.session['bid']
        forms = [form.cleaned_data for form in form_list]
        # print(forms)
        # self.request.session['forms'] = forms
        address = CheckOutAddressForm(data=forms[0])
        payment = CheckOutCCForm(data=forms[1])
        payment.save(commit=False)
        payment.bid = bid_id
        add = address.save()
        pay = payment.save()
        print(add)
        print(pay)
        # order = CheckOutConfirmForm(initial={'billing_address': add, 'payment_info': pay, 'buyer': buyer})
        Order.objects.update_or_create(billing_address=add, payment_info=pay, buyer=buyer_pro)
        close_bid = Bid.objects.get(id=bid_id)
        close_bid.StatusID = Status.objects.get(id=4)
        close_bid.save()
        # print("Her er order")
        # print(order)
        # if order.is_valid():
        #     print(order)
        #     order.save()
        context = {
            'forms': forms,
        }
        if self.request.user.is_authenticated:
            context['profile_info'] = Profile.objects.filter(user=self.request.user).first()
        return render(self.request, 'user/checkout/show_order.html', context)
        # return redirect('home')


def begin_check_out(request, id):
    request.session['bid'] = id
    # print(request.session['bid'])
    return redirect('check_out')


def mark_bid_closed(request):
    cur_bid = Bid.objects.get(id=request.session['bid'])
    cur_bid.StatusID = Status.objects.get(id=4)
    return redirect('profile')

