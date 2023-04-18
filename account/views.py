from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
#from django.views,generic.list import listView
#from django.views,generic.detail import DetailView


# Create your views here.



def register(request):
    form =SignUpForm()
    form2 = CustomerForm()
    if request.method =="POST":
        form=SignUpForm(request.POST)
        form2=CustomerForm(request.POST)

        if form.is_valid() and form2.is_valid():
            user =form.save()
            customer = form2.save(commit =False)
            customer.user = user
            customer.save()
            messages.success(request,'account successfully created')
            return redirect('account:login')

        context ={'form':form,'form2':form2}    
        return render(request, 'register.html', context)    

    context={'form':form,'form2':form2}   
    return render(request, 'register.html', context)  



def loginPage(request):

    form=LoginForm()
    if request.method == 'POST':

       # form=LoginForm(request.POST)
        form =AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                
                messages.info(request,"login successful")
                return redirect('/')

            messages.info(request,"User not found")  
            return render(request,'login.html') 

        #messages.info(request,"form not valid")        
    context ={'form':form}
    return render(request,'login.html',context)



#def Tasklist(request):
   # model= Task
    #context_object_name = 'tasks'

def Tasklist(request):
    #item = Task.objects()
    #context ={'task':task}
    return render(request,'task_.html')

def logoutPage(request):

    logout(request)
    return redirect('/')



def alltodo(request):
    task=mytodos.objects.all()
    form =TodoForm()
    if request.method=='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully submitted!")
            return redirect('account:todo')
    return render (request,'alltodo.html',{'task':task,'form':form})



def deleteItem(request,pk):
    task = mytodos.objects.get(id = pk)
    task.delete()
    return redirect('account:todo')


def navePages(request):
    
    return render (request,'index.html')    



def updateItem(request,pk):
    todo=mytodos.objects.get(id = pk)
    updateForm = TodoForm(instance = todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST,instance = todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('account:todo')
    return render (request,'updateitem.html',{'todo':todo, 'updateForm':updateForm})

