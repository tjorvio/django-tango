from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="product-index"),
    path('<int:id>', views.get_product_by_id, name="product-details"),
    path('categories/<int:id>', views.category_view, name="category-index"),
    path('create_product', views.create_product, name="create_product"),
    path('search_results', views.search_results, name="search_results"),
    path('edit_product/<int:id>', views.edit_product, name="edit_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
]
