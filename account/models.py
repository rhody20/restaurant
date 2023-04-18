from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Task(models.Model):
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank =True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


        class Meta:
            ordering = ['complete']



class mytodos(models.Model):
    task = models.TextField(max_length=100)
    def __str__(self):
        return self.task


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="customer_demands")
    phone_number=models.IntegerField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    addr = models.CharField(max_length=50)


    def __str__(self):
        return self.user.username



     
    
       
