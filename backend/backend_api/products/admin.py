from django.contrib import admin
from products.models import *
# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 0

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields if field.name != 'created_at']
    exclude = ("meanReview",)
    # inlines = [ProductImageInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
# ----------------------------- Dont need it now

# class ProductImageAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ProductImage._meta.fields]

#     class Meta:
#         model = ProductImage

# admin.site.register(ProductImage, ProductImageAdmin)

#------------------------------


# class ProductLogoAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ProductLogo._meta.fields]

#     class Meta:
#         model = ProductLogo

# admin.site.register(ProductLogo, ProductLogoAdmin)

class CategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class ReviewAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Reviews._meta.fields if field.name != "posted_on"]

    class Meta:
        model = Reviews

admin.site.register(Reviews, ReviewAdmin)

class ReviewLineAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ReviewLine._meta.fields]

    class Meta:
        model = Reviews

admin.site.register(ReviewLine, ReviewLineAdmin)