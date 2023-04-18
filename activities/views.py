
from multiprocessing import context
from re import M
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.


def  home(request):
    smooth=Smoothie.objects.all()
    number = Smoothie.objects.count()

    context ={'smooth':smooth, 'number':number}
    return render(request,"drinks.html", context)

    



def  about(request):
    return render(request,'about_us.html')  


def  contact(request):
    return render(request,'contactUs.html')    


def  fun(request):
    bb=int(request.POST.get('a'))
    tt=int(request.POST.get('t'))
    ff=bb + tt
    print(type(ff),ff)
    context={'ff':ff}
    return render(request,'result.html',context)


    
def form_link(request):
    return render (request,"base.html")


#funct0in to link to parents form page
def parentPage(request):
    return render(request,'data_form.html')   


def s_link(request):
    return render(request,'students_details.html')     


def student(request):
    if request.method == 'POST':

        fname=request.POST.get('f_name')
        l_name=request.POST.get("l_name")
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        email=request.POST.get("email")
        matric=request.POST.get("matric")
        #gender=request.POST.get("sex")
    
        
        StudentInformation.objects.create(first_name =fname,last_name=l_name,username=username, password=pass1,email=email,matric=matric)
        #print(f_name,l_name,username,passwrd,matric,gender)
        context={
        
        
        }

        return render(request,"basic.html",context)


def  parents(request):
    
    if request.method =='POST':

      f_name=request.POST.get("f_name")
      l_name=request.POST.get("l_name")
      username=request.POST.get("email")
      child=request.POST.get("child")
      klass=request.POST.get("child_class")
      tiTle=request.POST.get("title")
     
      print(f_name,l_name,username,child,klass,tiTle)
      context={
        'f_name':f_name,
        'l_name':l_name,
        'email':username,
        'password':child,
         'matric':klass,
        "tiTLE":tiTle,
        }
    
      return render(request,'about_us.html', context)



def studentsDetails(request):

    if request.method =="POST":

        fname= request.POST("f_name") 
        l_name=request.POST("l_name")  

        username=request.POST("username") 

        email=request.POST("email")
        pass1=request.POST("password1")

        pass2=request.POST("password2")
        print(pass2)
        StudentInformation.objects.create(first_name =fname,last_name=l_name,username=username, password=pass1,email=email) 


        return render(request,'success.html')







def bookingInfo(request):
     if request.method =="POST":
        namees=request.POST.get("namees")
        reserv_no=request.POST.get("reserv_no")
        email=request.POST.get("email")
        date=request.POST.get("date")
        BookingInfo.objects.create(namees=namees,reserv_no=reserv_no,email=email,date=date) 
        return render(request,"success.html")

     return render( request,"booking.html")



def church_info(request):
    if request.method =="POST":
       church_name =request.POST.get("church_name")  
       home_cell=request.POST.get("home_cell")
       vertual_church= request.POST.get("vertual_church")
       pastor_name =request.POST.get("pastor_name")
       date_joined=request.POST.get("date_joined")
       Church.objects.create(church_name=church_name,home_cell=home_cell,vertual_church=vertual_church,pastor_name=pastor_name,date_joined=date_joined )
       return render(request,"potal.html")
    return render(request,"church.html") 



def viewData(request):
    obj=Church.objects.all()
    num=obj.count()
    length = len(obj)

    context ={"rhoda":obj, 'num':num,'length':length }
    return render(request,"view_date.html",context)


def succeed(request):
    cal= BookingInfo.objects.all()
    lenght=len(cal)
    context={"show":cal,"lenght":lenght}
    return render(request,"success.html",context)


def showItem(request,pk):
    item=BookingInfo.objects.get(id=pk)
    context ={'item':item}
    return render(request,'single_item.html',context)



def deletedItem(request,pk):
    item=BookingInfo.objects.get(id=pk)
    item.delete()
    messages.info(request,'item succesfully deleted')
    return redirect('/')




def Church_information(request):
    form=ChurchForm()
    if request.method == "POST":
        form=ChurchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request, 'churchy.html',context)


def Books(request):
    hotels=Booknow()
    if request.method == 'POST':
        hotels=Booknow(request.POST)
        if hotels.is_valid():
            hotels.save()
            return  redirect ('/')

    context = {'hotels':hotels}
    return render (request,'booking_success.html', context) 



def shoPPERS(request):
    shoper=Shoppers()
    if request.method == 'POST':
        shoper=Shoppers(request.POST)
        if shoper.is_valid():
            shoper.save()
            return redirect ('/')
    context = {'shoper':shoper}
    return render (request,'navbar.html',context) 



def updateBooking(request,pk):
    item=BookingInfo.objects.get(id=pk)
    form=UpdateBookingForm( instance=item)

    if request.method == "POST":
        form =UpdateBookingForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request,'Successfully updated')
            return redirect('activities:show')

    
    context={'form':form}

    return render(request, 'update_booking.html', context)    


def aboutUs(request):
    return render(request, 'aboutUs.html')


def smoothie_site(request):
    pass



def orderInfo(request, id):
    item = Smoothie.objects.get(id=id)
    context ={'item':item}
    return render(request,'single_CLM.html', context)
   
    
def backEnd(request):
    item= Smoothie.objects.get(id=id)
    context ={'item':item}
    return render (request,'backpage.html', context)
    

def otherPages(request):

    return render(request,'form.html')



def submitOrder(request):
    if request.user.is_authenticated:
        item = request.POST.get('product_name')
        price = request.POST.get('price')
        
        if request.method == 'POST':
            Order.objects.create(customer = request.user,product_name=item, price=price)
            messages.info(request,'your order was sucessful')
            return redirect('/')
            
    messages.info(request,'please log in to make order ')
    return redirect('/')
    




def customer_item(request):
    if not request.user.is_authenticated:
        messages.info(request,' Please login to view your cart items.')
        return redirect('/')
    
    #customer=request.user
    if Order.objects.filter(customer=request.user).exists():
        customerInfo=Order.objects.filter(customer=request.user,payment=False)
        number = Order.objects.filter(customer=request.user,payment=False).count()
    
        total=0
        for item in customerInfo:
            price=int(item.price[1:])
            total += price 
    
        context={'customerInfo':customerInfo,'total':total,'number':number}
        return render(request,'customer_item.html',context)


    messages.info(request,'Please make some orders.')
    return redirect('/')
    
    

def delete_product(request,pk):
    item=Order.objects.get(id=pk).delete()
    #item.delete()
    messages.info(request,'item succesfully deleted')
    return redirect('activities:customer_order')



def payDetail(request):
    customerInfo=Order.objects.filter(customer=request.user)
    firstname = request.user.first_name
    lastname = request.user.last_name
    total=0
    for item in customerInfo:
        price=int(item.price[1:])
        total += price

    context={
        'total':total, 'firstname':firstname,'lastname':lastname
    }    
    return render (request,'payDetail.html',context)
  

    
   
        
#def back_end(request):
   # if request.method == 'POST':
        #full_name = request.POST("full_name")
        #card_details = request.POST("card_details")
        #amount_paid = request.POST("amount_paid")
        #BackEnd.objects.create(full_name =full_name,card_detail = card_details,amount_paid= amount_paid)
        #messages.info(request,'your order was sucessful')
        #return redirect('/')
    #return render (request,'backpage.html')

def PaymentInfo(request):
    form = Payment_details()
    if request.method =="POST":
        form=Payment_details(request.POST)
        if form.is_valid():
            form.save()
            Order.objects.filter(customer = request.user).update(payment=True)
            
            messages.info(request,'thank you for your patronage')
            return redirect('/')

        if form.errors:
            print(form.errors)

    messages.info(request,'Please check your bank details and try again.')
    return redirect('activities:customer_order')









        
        


    
   







