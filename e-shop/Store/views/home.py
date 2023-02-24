from django.shortcuts import render, redirect
from Store.models.product import Product
from Store.models.category import Category
from django.views import View


# Create your views here.

class Index(View):
    def post(self, request):
        product=request.POST.get("product")# 'product' taken from index.html  name of input attribute
        remove=request.POST.get("remove")# 'remove' taken from index.html  name of input attribute
        cart=request.session.get("cart")
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                       cart[product] = quantity-1
                else:
                   cart[product] = quantity+1 
            else:
                cart[product]=1
        else :    
            cart={}
            cart[product]=1
        request.session["cart"]=cart
        print(cart)
        return redirect("Homepage")

    def get(self, request):
      cart=request.session.get("cart")
      if not cart:
        request.session["cart"]={}
      products=None 
      categories=Category.get_all_categories()
      categoryID=request.GET.get('category')
      if categoryID:
        products=Product.get_all_products_by_categoryid(categoryID)
      else:
        products=Product.get_all_products()
      data={}
      data['products']=products
      data['categories']=categories
      print("you are: ", request.session.get("email"))
      return render(request, "index.html", data)