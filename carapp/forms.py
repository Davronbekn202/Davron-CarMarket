from django import forms
from .models import Category,Car,LocationOfProduct

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'title',
            'description',
            'price',
            'color',
            'year',
            'mileage',
            'condition',
            'image',
            'phone_number',
            'category',
        ]


