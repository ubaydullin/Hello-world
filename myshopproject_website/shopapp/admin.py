from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content', 'price','created_at')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','phone')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'phone', 'email')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Contact, ContactAdmin)


