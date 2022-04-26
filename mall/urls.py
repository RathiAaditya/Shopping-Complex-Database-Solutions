from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer',views.customerdata,name='customer'),
    path('company',views.companydata,name='company'),
    path('invoice',views.invoicedata,name='invoice'),
    path('company/search',views.searchcompany,name='companysearch'),
    path('customer/search',views.searchcustomer,name='customersearch'),
    path('contract',views.contractdata,name='contract'),
    path('geninvoice',views.generateInvoice,name='geninv')
]
