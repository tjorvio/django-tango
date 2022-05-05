from django.shortcuts import render, get_object_or_404, redirect

from FireSale.forms.user_form import UserCreateForm
from user.models import Country, Payment
from user.models import User


def index(request):
    # return render(request, 'product/index.html', context={'products': products})
    context = {'user': User.objects.all().order_by('name')
               }
    return render(request, 'user/index.html', context)


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_image = User(picture=request.POST['picture'], user=user)
            user_image.save()
            return redirect('user-index')
    else:
        form = UserCreateForm()

    return render(request, 'user/create_user.html', {
        'form': form
    })
