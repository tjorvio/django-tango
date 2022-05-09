from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="user-index"),
    path('place_bid', views.place_bid, name="place_bid"),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('accept/<int:id>', views.accept_bid, name='accept_bid'),
    path('decline/<int:id>', views.decline_bid, name='decline_bid'),
]