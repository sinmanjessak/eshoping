from django.urls import path
from .views import index,signup,login

urlpatterns = [

   path('',index.Index.as_view(),name= 'home'),
   path('signup',signup.Signup.as_view(), name='signuppage'),
   path('login',login.Login.as_view(), name='loginpage')
]
