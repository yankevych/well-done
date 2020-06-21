from django.contrib import admin

from .models import Portfolio, PostsImages


class InlineImage(admin.TabularInline):
    model = PostsImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineImage]


admin.site.register(Portfolio, ProductAdmin)
