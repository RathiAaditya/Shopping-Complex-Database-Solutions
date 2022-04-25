from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from mall.models import Companies, Customer, Invoice
# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    username = request.POST['Username']
    password = request.POST['Password']
    if username == 'Aaditya' and password == '1234':
        return render(request, 'home.html', {'name': username})
    else:
        messages.info(request, 'Invalid Credentials')
        return redirect('/')


def customerdata(request):
    customers = Customer.objects.all()
    all_fields = [field.name for field in Customer._meta.get_fields()]
    del all_fields[0]
    flag = True
    return render(request, 'customerdata.html', {'customer': customers, 'column': all_fields, 'fl': flag})


def companydata(request):
    companies = Companies.objects.all()
    all_fields = [field.name for field in Companies._meta.get_fields()]
    del all_fields[0:4]
    flag = True
    return render(request, 'companydata.html', {'company': companies, 'column': all_fields, 'fl': flag})


def invoicedata(request):
    invoices = Invoice.objects.all()
    all_fields = [field.name for field in Invoice._meta.get_fields()]
    del all_fields[0]
    return render(request, 'invoicedata.html', {'invoice': invoices, 'column': all_fields})


def searchcompany(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        searched = Companies.objects.filter(name__icontains=search_id)
        all_fields = [field.name for field in Companies._meta.get_fields()]
        del all_fields[0:4]
        flag = False
        return render(request, 'companydata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchcustomer(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        searched = Customer.objects.filter(firstname__icontains=search_id)
        all_fields = [field.name for field in Customer._meta.get_fields()]
        del all_fields[0]
        flag = False
        return render(request, 'customerdata.html', {'search': searched, 'column': all_fields, 'fl': flag})
