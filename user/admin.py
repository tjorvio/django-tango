from django.contrib import admin
from user.models import Status, Profile, Payment, Country, Bid
# Register your models here.
admin.site.register(Status)
admin.site.register(Profile)
admin.site.register(Payment)
admin.site.register(Country)
admin.site.register(Bid)

