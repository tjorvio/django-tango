from django.core.validators import MinValueValidator, MaxValueValidator
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
    Bio = models.CharField(max_length=255, default=None, null=True)
    CountryID = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


class Bid(models.Model):
    BidAmount = models.FloatField(default=0)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    StatusID = models.ForeignKey(Status, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ProductID.name} + Bid: €{self.BidAmount}"

class Order(models.Model):
    # Contact info ---
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.IntegerField()
    CountryID = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    # Payment info --
    cardholder = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    expire_month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    expire_year = models.IntegerField(validators=[MinValueValidator(00), MaxValueValidator(99)])
    card_cvc = models.IntegerField(validators=[MinValueValidator(000), MaxValueValidator(999)])
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)

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
