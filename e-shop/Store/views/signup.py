from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  #for hashing password
from Store.models.customer import Customer
from django.views import View


class Signup(View):
  def get(self, request):
     return render(request,'signup.html')

  def post(self, request): 
      postData=request.POST
      first_name=postData.get('firstname')#This  "firstname" is the value which we have given in "signup.html" in first_name input name
      last_name=postData.get('lastname')
      phone=postData.get('phone')
      email=postData.get('email')
      password=postData.get('password')
       
 
      
# If there is any error in form fill up, it will be given by error_message , but this
# value variable will keep other filled values as it is, without erasing it. 
      

       
      value={
            "first_name" : first_name,
            "last_name" : last_name,
            "phone" : phone,
            "email" : email,
          }

      error_message=None

      customer=Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        
      error_message=self.validateCustomer(customer)
        # saving
      if not error_message:
        #  print(first_name, last_name, phone, email, password)
         customer.password=make_password(customer.password) #for hashing password
         customer.register()
         return redirect("Homepage")
      else:
         data= {
            "error" : error_message,
            "values" : value             #Name "values" is linked in sigup.html in input value.
         }
         return render(request, "signup.html", data)              
  
  def validateCustomer(self, customer):
        error_message=None
        if not customer.first_name:
            error_message="First Name Required"
        elif len(customer.first_name)<4:
                error_message="First Name should be 4 char long or more"
        elif not customer.last_name:
            error_message="Last Name Required"
        elif len(customer.last_name)<4:
                error_message="Last Name should be 4 char long or more"
        elif not customer.phone:
            error_message="Phone Required"
        elif len(customer.phone)<10:
                error_message="Phone should be 10 char long or more"
        elif not customer.email:
            error_message="Email Required"
        elif len(customer.email)<5:
                error_message="Email should be 5 char long or more"
        elif not customer.password:
            error_message="password Required"
        elif len(customer.password)<6:
                error_message="Password should be 6 char long or more"
        elif customer.isExists():
                error_message="Email Already Exists"
        return error_message
