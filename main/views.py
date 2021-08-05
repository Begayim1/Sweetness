from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from shop.models import Category, Product
from .forms import RegistrationForm


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')



class SingInView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('home')


# def home(request):
#     categories = Category.objects.all()
#     print(categories)
#     return render(request, 'shop/home.html', {'title': 'Главная страница', 'categories': categories})
#
# def list(request):
#     products = Product.objects.all()
#     return render(request, 'shop/list.html', {'title': ' страница', 'products': products})
#
#
#
# def basket(request):
#     return render(request, 'shop/basket.html')
#
#
# def contacts(request):
#     return render(request, 'shop/contacts.html')
#
#
# def favorites(request):
#     return  render(request, 'shop/favorites.html')