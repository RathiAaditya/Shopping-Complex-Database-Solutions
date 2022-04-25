from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('home/customer', views.customerdata, name='customer'),
    path('home/company', views.companydata, name='company'),
    path('home/invoice', views.invoicedata, name='invoice'),
    path('home/company/search', views.searchcompany, name='companysearch'),
    path('home/customer/search', views.searchcustomer, name='customersearch'),
]
