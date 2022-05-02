from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=9999, blank=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    #sellerID = models.ForeignKey(User, on_delete=models.CASCADE)
    CreatedAt = models.TimeField(blank=True)
    SoldOrNot = models.IntegerField(blank=True)
    #ConditionID = models.ForeignKey(Condition, on_delete=models.CASCADE)

