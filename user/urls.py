from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path

from . import views
from .forms.checkout_address_form import CheckOutAddressForm
from .forms.checkout_cc_form import CheckOutCCForm
from .forms.checkout_confirm_form import CheckOutConfirmForm
from .views import OrderWizard

forms = (
    ('address', CheckOutAddressForm),
    ('cc', CheckOutCCForm),
    # ('confirmation', CheckOutConfirmForm)
)

order_wizard = OrderWizard.as_view(forms, url_name='order_step', done_step_name='finished')

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
    path('seller_profile/<int:id>', views.seller_profile, name='seller_profile'),
    # path('check_out/<int:id>', views.check_out1, name='check_out'),
    # path('payment', views.check_out2, name='check_out2'),
    path('begin_check_out/<int:id>', views.begin_check_out, name='begin_check_out'),
    re_path(r'^checkout/(?P<step>.+)/$', order_wizard, name='order_step'),
    path('checkout/', order_wizard, name='check_out'),
    path('checkout/closed', views.mark_bid_closed, name='mark_bid_closed'),
]