from django.shortcuts import render
#from django.http import HttpResponse
products = [
    {'name': 'Smart Tv',
     'price': 20.0,
     'description': 'An LG smart tv, with remote and power cable',
     'category': 'Electronics'
     },
    {'name': 'Dr. Martin boots',
     'price': 10.0,
     'description': 'Nearly new, no wear and tear. Don´t smell',
     'category': 'Fashion'
     }
]
# Create your views here.
def index(request):
    return render(request, 'product/index.html', context={'products': products})

def home_view(request):
    return render(request, 'home.html')