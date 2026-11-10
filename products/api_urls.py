from django.urls import path
from . import views

app_name = "products_api"
urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product-list'),
    path('<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]
