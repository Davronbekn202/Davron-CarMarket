from django import forms
from .models import Car,LocationOfProductModel


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
            'other_brand',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mashina nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mashina haqida ma’lumot', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Narxi'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rangi'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ishlab chiqarilgan yil'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Yurgani (KM)'}),
            'condition': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'other_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agar boshqa marka bo‘lsa yozing'}),
        }

        labels = {
            'title': 'Mashina nomi',
            'description': 'Tavsif',
            'price': 'Narxi',
            'color': 'Rangi',
            'year': 'Ishlab chiqarilgan yil',
            'mileage': 'Yurgani (KM)',
            'condition': 'Holati',
            'image': 'Rasm',
            'phone_number': 'Telefon raqam',
            'category': 'Kategoriya',
            'other_brand': 'Boshqa marka',
        }
class LocationOfProductForm(forms.ModelForm):
    class Meta:
        model = LocationOfProductModel
        fields = ['city','street','home','house']
