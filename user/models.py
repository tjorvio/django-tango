from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import Product


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Payment(models.Model):
    PaymentMethod = models.CharField(max_length=255)
    PreferredPayment = models.BooleanField(default=0)

    def __str__(self):
        return self.PaymentMethod


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StreetName = models.CharField(max_length=255)
    Zip = models.FloatField(default=0)
    City = models.CharField(max_length=255)
    Picture = models.CharField(max_length=255)
    CountryID = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


class Bid(models.Model):
    BidAmount = models.FloatField(default=0)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    StatusID = models.ForeignKey(Status, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ProductID.name} + Bid: €{self.BidAmount}"

# class Order(models.Model):
#     cardholder = models.CharField(max_length=255)
#     card_number = models.CharField(max_length=16, validators=MinLengthValidator(16, 'Card number needs 16 digits'))
#     expire_month = models.IntegerField(max_length=2, validators=MinLengthValidator(2, 'Please use 2 digits for month'))
#     expire_year = models.IntegerField(max_length=2, validators=MinLengthValidator(2, 'Please only use 2 digits for year'))
#     card_cvc = models.IntegerField(max_length=3, validators=MinLengthValidator(3, 'CVC number needs 3 digits'))
#     bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
#     buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Rating(models.Model):
    stars = models.FloatField(default=0)
    count = models.FloatField(default=0)
    UserID = models.ForeignKey(Profile, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
