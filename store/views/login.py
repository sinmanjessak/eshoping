from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.views import View

class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email= request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)

        customer= Customer.get_customer_by_email(email)
        msg=None
        if customer:
            flag= check_password(password,customer.password)
            if flag:
               messages.info(request," You Successfully Logged in!")
               request.session['customer_id']= customer.id         #for checking session (Extra)
               request.session['email']=customer.email
               return redirect('/')
            else:
               messages.error(request,"Password did't Match!!")
               msg= "password did't Match!!"
               return render(request, 'login.html', {'error': msg})
        else:
           return render(request, 'login.html')
