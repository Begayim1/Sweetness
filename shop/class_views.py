from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView

from shop.forms import CreateShopForm, UpdateShopForm
from shop.models import Category, Product


class SearchListView(ListView):
    model = Product  # Product.objects.all()
    template_name = 'shop/search.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        # print(self.request.GET)
        q = self.request.GET.get('q')
        if not q:
            return Product.objects.none()
        queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return  queryset


class CategoryListView(ListView):
    model = Category  # Category.object.all()
    template_name = 'shop/home.html'
    context_object_name = 'categories'


class ShopListView(ListView):
    model = Product   # Product.object.all()
    template_name = 'shop/list.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(category__slug=slug)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get('slug')
        return context


class ShopDetailView(DetailView):
    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'


class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


class ShopCreateView(IsAdminCheckMixin, CreateView):
    model = Product
    template_name = 'shop/create_product.html'
    form_class = CreateShopForm
    # context_object_name = 'product_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


class ShopUpdateView(IsAdminCheckMixin, UpdateView):
    model = Product
    template_name = 'shop/update_product.html'
    form_class = UpdateShopForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


class ShopDeleteView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'shop/delete_product.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('home')

# class ShopListView():
#     model = Product
#     template_name = 'shop/list.html'


class ShopFavoritesView(ListView):
    model = Product
    template_name = 'shop/favorites.html'
    pk_url_kwargs = 'id'


class ShopContactsView():
    pass