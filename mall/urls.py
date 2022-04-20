from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('login', views.login, name='login'),
    path('customer',views.customerdata,name='customer'),
    path('company',views.companydata,name='company')
]
