# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path
#
#
# from . import views
# #
# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('list/', views.list, name='list'),
#     path('basket/', views.basket, name='basket'),
#     path('favorites/', views.favorites, name='favorites'),
#     path('contacts/', views.contacts, name='contacts'),
# #
#               ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib.auth.views import LogoutView
from django.urls import path

from main.views import *
from shop.class_views import SearchListView, ShopUpdateView, ShopDeleteView, ReviewAdd

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SingInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/update/<int:id>', ShopUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:id>', ShopDeleteView.as_view(), name='update_product'),
    path('search', SearchListView.as_view(), name='search'),
    path('add-review/<int:id>/', ReviewAdd.as_view(), name="add-review")
]