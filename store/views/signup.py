from django.shortcuts import render,redirect
from store.models.customer import Customer 
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
   def get(self,request):
      return render(request,"signup.html") 
   
   def post(self,request):
      post_data= request.POST
      first_name= post_data.get('first_name')
      last_name= post_data.get('last_name')
      email= post_data.get('email')
      phone = post_data.get('phone')
      password1= post_data.get('password1')
      password2= post_data.get('password2')

 # _____>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>VALIDATIONS...validation in signup form  ...
      error_msg = None 

      if password1 == password2 :
         if Customer.objects.filter(email=email).exists():
            error_msg = "Email already Exists!!"
            return render(request,"signup.html",{'error':error_msg})   
         else:
            customer = Customer(first_name= first_name,last_name=last_name,email=email,phone=phone,password=password1)
            customer.password= make_password(customer.password)
            customer.save()
            return redirect('loginpage')
      else:
         error_msg= "Password did't Match!!"
         return render(request,"signup.html",{'error':error_msg})