from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'product/index.html')

def home_view(request):
    return render(request, 'home.html')