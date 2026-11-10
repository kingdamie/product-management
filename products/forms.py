from django import forms
from .models import Product


# A ModelForm builds the HTML form and the validation from the model.
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price']
