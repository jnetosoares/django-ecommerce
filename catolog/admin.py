from django.contrib import admin

# Register your models here.

from .models import Category, Product

class ProductInLine(admin.StackedInline):
    model = Product
    #extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','created','modified']
    search_fields = ['name']
    list_filter = ['name','created']
    inlines = [ProductInLine]





# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name','slug','created','modified']
#     search_fields = ['name']

admin.site.register(Category,CategoryAdmin)

#admin.site.register(Product,ProductAdmin)
