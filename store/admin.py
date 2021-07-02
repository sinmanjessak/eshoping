from django.contrib import admin
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer

class AdminProduct(admin.ModelAdmin):
   list_display=['id','name','price','category']

class AdminCategory(admin.ModelAdmin):
   list_display=['id','name']

class CustomerAdmin(admin.ModelAdmin):
   list_display=['id','first_name','last_name','email','phone','password']



admin.site.register(Customer,CustomerAdmin)
admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)


