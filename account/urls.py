from django.urls import path
from .import views


app_name='account'




                                                                                                                                                                                                                                                                                                                                                                                                                
urlpatterns=[
path('signUP/',views.register,name='signUP'),
path('login/',views.loginPage,name='login'),
path('task/',views.Tasklist,name='task'),
path('logout/',views.logoutPage,name='logout'),
path('todo/',views.alltodo,name='todo'),
path('deleteitem/<int:pk>/', views.deleteItem,name='deleteitem'),
path('updateitem/<int:pk>/', views.updateItem,name='updateitem'),
path('navkey/',views.navePages,name='navkey'),


]