from django import forms

from .models import Product, Review


class CreateShopForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class UpdateShopForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['product']