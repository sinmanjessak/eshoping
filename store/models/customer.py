from django.db import models


class Customer(models.Model):
   first_name=models.CharField(max_length= 100,default=None,null=True)
   last_name= models.CharField(max_length=100,default= None,null=True,blank=True)
   email= models.EmailField(unique=True)
   phone = models.PositiveIntegerField(default=None,null=True,blank=True)  
   password= models.CharField(max_length=50)


   @staticmethod
   def get_customer_by_email(email):
      try:
         return Customer.objects.get(email=email)
      except:
         return False

   

      

