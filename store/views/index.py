from django.shortcuts import render,redirect
from store.models.category import Category
from store.models.product import Product
from django.views import View

class Index(View):
    def get(self,request):
        products = None
        Categories = Category.get_all_categories()#Category.objects.all()...

        categoryid = request.GET.get('category') # to search  categories by categories id..
        print(categoryid)
        if categoryid:
            products = Product.get_all_products_by_id(categoryid) # for searching categories wise..
        else:
            products = Product.get_all_products()

        data = {}
        data['Products'] = products
        data['Categories'] = Categories
        print("you session email are ", request.session.get('email')) #FOR check session email which are logged in...

        return render(request, 'index.html', data)

    def post(self,request):
        product= request.POST.get('product')
        remove= request.POST.get('cart') # Make responsive  "Add to Cart" button
        #  create cart in session..
        #       ___________________________________________
        cart= request.session.get("cart")       #access cart from session
        if cart:                 #check cart is present or not.. if present we add product..
            quantity= cart.get(product)# we define quantity..
            if quantity <=1 :
                if remove:
                    if quantity <=1:

                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    #ifcustomer add product ...
                    cart[product]= quantity + 1  # we increase product.in cart
            else:
                cart[product]=1    # else nothing
        else:
            cart={}   # else cart is not present ..it gives None
            cart[product]=1
        request.session['cart']=cart   #again we add cart in session....(because we add product in cart..so that's why we add cart in session for we check  how much product add in session...)
        print("cart:>>",request.session['cart'])
        return redirect('/')
