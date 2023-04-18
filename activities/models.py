
from dataclasses import fields
from distutils.command.upload import upload
import email
from pyexpat import model
from django.db import models
from account.models import *

# Create your models here.



class StudentInformation(models.Model):
    first_name =models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    matric=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name




class BookingInfo(models.Model):
    namees=models.CharField(max_length=50)
    reserv_no=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    date=models.DateField(max_length=30)

    def __str__(self):
        return self.namees


class Church(models.Model):
    church_name =models.CharField(max_length=100)
    home_cell =models.CharField(max_length=50)
    vertual_church= models.CharField(max_length=50)
    pastor_name= models.CharField(max_length=40)
    date_joined=models.DateField()

    def  __str__(self):
        return self.church_name





class Smoothie(models.Model):
    
    prod_name=models.CharField(max_length=100)
    discrption=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    availability=models.CharField(max_length=300)
    image = models.ImageField(upload_to='pic',null=True, blank=True)

    def __str__(self):
        return self.prod_name



class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.CharField(max_length=10,null=False,blank= False)
    product_name= models.CharField(max_length=100,null=False,blank=False)
    payment = models.BooleanField(default=False)
    create= models.DateField(auto_now_add=True)
                                                                                                                                                                                                                                                        
    def __str__(self):
        return str(self.customer)

    def getTotal(self):
        total =0
        for p in int(self.price[1]):
            total += p    
            return total

 

class PaymentDetails(models.Model):
    fullname=models.CharField(max_length=100)
    card_details=models.IntegerField()
    total=models.IntegerField()
    date_paid= models.DateField(auto_now_add=True)

    def  __str__(self):
        return self.fullname
    
