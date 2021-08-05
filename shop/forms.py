from django import forms

from .models import Product
class CreateShopForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class UpdateShopForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'