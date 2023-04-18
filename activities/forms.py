from msilib.schema import Class
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import *



class ChurchForm(forms.ModelForm):
    #Widget={'date_joined':forms.DateField()}
    class Meta:
        model=Church
       # fields = ['church_name','home_cell','vertual_church','pastor_name','date_joined']
        fields ='__all__'



class Booknow(forms.ModelForm):
    class Meta:
        model=BookingInfo
        fields='__all__'
        



class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model=BookingInfo
        fields='__all__'




class Shoppers(forms.ModelForm):
    class Meta:
        model=StudentInformation
        fields='__all__'


        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=('customer',) 



class Payment_details(forms.ModelForm):
    class Meta:
        model=PaymentDetails
        fields=('fullname','card_details','total')
