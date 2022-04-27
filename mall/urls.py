from django.urls import path
from . import views

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
    path('home/invoice/search', views.searchinvoice, name='invoiceserach'),
]
