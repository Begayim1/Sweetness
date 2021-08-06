from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class Category(models.Model):

    name = models.CharField(max_length=55, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} {self.name}'
        return self.name


class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')

    )

    name = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("detail", kwargs={'id': self.id})

    class Meta:
        ordering = ['-id']


class Review(models.Model):
    user = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="review", verbose_name='продукты', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return "Comment by {} on {}".format(self.user, self.product)
