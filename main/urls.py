from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('basket/', views.basket, name='basket'),
    path('favorites/', views.favorites, name='favorites'),
    path('contacts/', views.contacts, name='contacts'),

]