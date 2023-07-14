from django.contrib import admin
from products.models import *
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)

class ProductLogoAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductLogo._meta.fields]

    class Meta:
        model = ProductLogo

admin.site.register(ProductLogo, ProductLogoAdmin)

class CategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)