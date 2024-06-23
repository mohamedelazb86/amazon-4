from django.contrib import admin
from .models import Post,Review,Category

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Review)

