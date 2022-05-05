from django.db import models
from product.models import Product


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255)


class Payment(models.Model):
    PaymentMethod = models.CharField(max_length=255)
    PreferredPayment = models.BooleanField(default=0)


class User(models.Model):
    Email = models.CharField(max_length=255)
    PasswordEncrypt = models.CharField(max_length=255)
    Username = models.CharField(max_length=255)
    StreetName = models.CharField(max_length=255)
    Zip = models.FloatField(default=0)
    City = models.CharField(max_length=255)
    Picture = models.CharField(max_length=255)
    PreferredPaymentID = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    CountryID = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Username

    def get_payment_id(self):
        return self.PreferredPaymentID


class Bid(models.Model):
    BidAmount = models.FloatField(default=0)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    BuyerID = models.ForeignKey(User, on_delete=models.CASCADE)
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    StatusID = models.ForeignKey(Status, default=1, on_delete=models.CASCADE)
