from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from FireSale.forms.make_bid_form import MakeBidForm


# Create your views here.
from user.forms.profile_form import ProfileForm
from user.models import Profile


def index(request):
    return render(request, 'user/index.html')

@login_required
def place_bid(request):

    if request.method == 'POST':
        form = MakeBidForm(data=request.POST)
        if form.is_valid():
            bid = form.save(commit=False)  # Save data as a bid model class, but don´t commit to database

            bid.save()  # Save all data in database
            return redirect('user-index')
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

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })
