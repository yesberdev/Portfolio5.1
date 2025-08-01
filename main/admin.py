from django.contrib import admin

# Register your models here.
from .models import Product, BlogMessage

admin.site.register(Product)

admin.site.register(BlogMessage)