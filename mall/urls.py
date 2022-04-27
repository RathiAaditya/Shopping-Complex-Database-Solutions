from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('home/contract', views.contractdata, name='contract'),
    path('geninvoice', views.generateInvoice, name='geninv'),
    path('home', views.home, name='home'),
    path('home/customer', views.customerdata, name='customer'),
    path('home/company', views.companydata, name='company'),
    path('home/invoice', views.invoicedata, name='invoice'),
    path('home/company/search', views.searchcompany, name='companysearch'),
    path('home/customer/search', views.searchcustomer, name='customersearch'),
    path('home/shop', views.shopdata, name='Shops'),
    path('home/shop/search', views.searchshop, name='shopsearch'),
    path('home/slot', views.slotdata, name='slotdata'),
    path('home/slot/search', views.searchslot, name='slotsearch'),
    path('home/booking', views.bookingdata, name='booking data'),
    path('home/booking/search', views.searchbooking, name='bookingsearch'),
    path('home/service', views.servicedata, name='servicedata'),
    path('home/service/search', views.searchservice, name='servicesearch'),
    path('home/provides', views.providesdata, name="provides"),
    path('otp', views.otp, name='otp'),
    path('home/invoice/search', views.searchinvoice, name='invoiceserach'),
    re_path(r'form/insertCompany', views.Companyform, name='insertCompany'),
    re_path(r'form/insertContract', views.Contractform, name='insertContract'),
    re_path(r'form/insertShop', views.Shopform, name='insertShop'),
    re_path(r'form/insertSlot', views.Slotform, name='insertSlot'),
    re_path(r'form/insertService', views.Servicesform, name='insertService'),
    re_path(r'form/insertCustomer', views.Customerform, name='insertCustomer'),
    path('home/receipt',views.receiptdata, name='receipt'),
    path('home/genrecpt',views.generateBooking,name='genrecpt')


]
