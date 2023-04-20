
from django.urls import path

from activities.models import Church
from .import views


app_name='activities'

urlpatterns=[
    path('',views.home,name='home'),
   path('about_us/',views.about,name='about_us'),
   path('contact_us/',views.contact,name='contact_us'),
   path('form/',views.fun,name='form'),
   path("formpage/",views.form_link,name="formpage"),
   path('pupils/',views.student ,name='pupils'),


   path('p_link/',views.parentPage,name='p_link'),
   path('shop/', views.s_link,name='shop'),

   path('parentsInfo/',views.parents,name='parentsInfo'),

   path('students_details/',views.studentsDetails,name='students_details'),

   path('booking/',views.bookingInfo,name='booking'),

   path('church/',views.church_info,name='church'),

   path('view_data/',views.viewData,name='view_data'),

   path('show/', views.succeed, name='show'),



 path('show_single_item/<int:pk>/', views.showItem, name='show_single_item'),

  path('delete_show/<int:pk>/', views.deletedItem, name='delete_show'),

  path('new_form/',views.Church_information,name='new_form'),

  path('bookNOW/',views.Books,name='bookNOW'),

  path('updated/',views.shoPPERS,name='updated'),

  path('booking_update/<int:pk>/',views.updateBooking,name='booking_update'),

  path('smoothie/',views.smoothie_site,name='smoothie'),

  path('abt_us/',views.aboutUs,name='abt_us'),
  path('order_/<int:id>/',views.orderInfo,name='order_'),
  path('endpage/<int:id>/',views.backEnd,name='endpage'),



  #path('endpage/',views.backEnd,name='endpage'),
  path('search-item/',views.searches,name='search-item'),
  
   path('others/',views.otherPages,name='others'),
   path('submitodER/',views.submitOrder,name='submitodER'),
   path('customer_order/', views.customer_item,name='customer_order'),
   path('delete-item/<int:pk>/', views.delete_product,name='delete-item'),
   path('pay/', views.payDetail,name='pay'),
   path('paid/', views.PaymentInfo,name='paid'),


   
  





   
   


]