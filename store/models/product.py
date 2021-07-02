from .category import Category
from django.db import models

class Product(models.Model):
   name=models.CharField(max_length=60)
   price= models.CharField(max_length=10,default=0)
   category= models.ForeignKey(Category ,on_delete= models.CASCADE,default=1)
   discription= models.CharField(max_length= 200,default="",null =True,blank=True)
   image= models.ImageField(upload_to=" UPLOADS/product/")


   def __str__(self):
      return self.name

   @staticmethod
   def get_all_products():
      return Product.objects.all()

   @staticmethod     # This is fuction for filtering products by category
   def get_all_products_by_id(category_id):
      if category_id:
         return Product.objects.filter(category=category_id)
      else:
         return Product.get_all_products()











