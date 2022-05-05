from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="user-index"),
    path('place_bid', views.place_bid, name="place_bid"),
]