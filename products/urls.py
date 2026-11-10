from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    # ex: /products/
    path("", views.product_list, name="list"),
    # ex: /products/add/
    path("add/", views.product_create, name="create"),
    # ex: /products/5/
    path("<int:product_id>/", views.product_detail, name="detail"),
    # ex: /products/5/edit/
    path("<int:product_id>/edit/", views.product_update, name="update"),
    # ex: /products/5/delete/
    path("<int:product_id>/delete/", views.product_delete, name="delete"),
]
