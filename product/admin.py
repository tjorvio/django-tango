from django.contrib import admin
from product.models import Product, Category, Condition, Reviews, Picture
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Condition)
admin.site.register(Reviews)
admin.site.register(Picture)

