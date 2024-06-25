from django.contrib import admin

from .models import Product,ProductImage,Brand,Review
from django_summernote.admin import SummernoteModelAdmin

class ProductImageAdmin(admin.TabularInline):
    model=ProductImage

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','flag','sku']
    search_fields=['name','subtitle','descriptions']
    list_filter=['flag','brand']

    summernote_fields = ('subtitle','descriptions')
    inlines=[ProductImageAdmin]

admin.site.register(ProductImage)
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
