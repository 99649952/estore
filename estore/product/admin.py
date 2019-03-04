from django.contrib import admin

from .models import Product
from .models import ProductImage
from .models import Category
from .models import Attribute
from .models import AttributeValue


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(AttributeValue, AttributeValueAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
