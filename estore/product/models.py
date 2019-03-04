from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=10)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='价格')
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product.name


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(
        Product, related_name='product_attributes', blank=True,
        null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True, default='')
    attribute = models.ForeignKey(
        Attribute, related_name='values', on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.name, self.value)

