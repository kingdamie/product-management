from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Product
from .serializers import ProductSerializer


# GET /products/  -> list all products
# POST /products/ -> add a product
class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer


# GET    /products/<id>/ -> single product
# PUT    /products/<id>/ -> full edit
# PATCH  /products/<id>/ -> partial edit
# DELETE /products/<id>/ -> delete
class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# ---------------------------------------------------------------------------
# Template (HTML) views
# ---------------------------------------------------------------------------
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm


def product_list(request):
    products = Product.objects.order_by('-created_at')
    return render(request, "products/product_list.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/product_detail.html", {"product": product})


def product_create(request):
    if request.method == "POST":
        # request.FILES holds the uploaded image
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect("products:detail", product_id=product.pk)
    else:
        form = ProductForm()
    return render(request, "products/product_form.html", {"form": form, "title": "Add product"})


def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        # instance=product makes this an update instead of a new row
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:detail", product_id=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, "products/product_form.html", {"form": form, "title": "Edit product"})


def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("products:list")
    return render(request, "products/product_confirm_delete.html", {"product": product})
