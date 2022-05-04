from django.db import models
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Condition(models.Model):
    condition = models.CharField(max_length=255)

    def __str__(self):
        return self.condition


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=9999, blank=True)
    CreatedAt = models.DateTimeField(default=now())
    SoldOrNot = models.IntegerField(default='0')
    sellerID = models.ForeignKey('user.User', on_delete=models.CASCADE)
    # Maybe we should not have Cascaded on deletion of ConditionID
    ConditionID = models.ForeignKey(Condition, on_delete=models.CASCADE)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)


class Picture(models.Model):
    picture = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture


