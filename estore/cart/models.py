from django.db import models
from django.conf import settings
from ..product.models import Product


class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name='加入购物车中的商品')
