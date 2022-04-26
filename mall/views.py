from asyncio.windows_events import NULL
from urllib import response
from django.http import HttpResponse
from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from mall.models import Booking, Companies, Customer, Invoice, Contracts, AdminModel, Shops, Slots

# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    if(request.method == 'POST'):
        usrname = request.POST['Username']
        pwd = request.POST['Password']
        adminuser = authenticate(username=usrname, password=pwd)
        if adminuser is not None:
            login(request, adminuser)
            return render(request, 'home.html', {'name': usrname})
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:

        adminname = request.user.username
        print(adminname)
        return render(request, 'home.html', {'name': adminname})


def customerdata(request):
    customers = Customer.objects.all()
    all_fields = [field.name for field in Customer._meta.get_fields()]
    del all_fields[0]
    flag = True
    return render(request, 'customerdata.html', {'customer': customers, 'column': all_fields, 'fl': flag})


def shopdata(request):
    shops = Shops.objects.all()
    all_fields = [field.name for field in Shops._meta.get_fields()]
    del all_fields[0]
    flag = True
    return render(request, 'shopdata.html', {'shop': shops, 'column': all_fields, 'fl': flag})


def slotdata(request):
    slots = Slots.objects.all()
    all_fields = [field.name for field in Slots._meta.get_fields()]
    del all_fields[0]
    flag = True
    return render(request, 'slotdata.html', {'slot': slots, 'column': all_fields, 'fl': flag})


def companydata(request):
    companies = Companies.objects.all()
    all_fields = [field.name for field in Companies._meta.get_fields()]
    del all_fields[0:4]
    flag = True
    return render(request, 'companydata.html', {'company': companies, 'column': all_fields, 'fl': flag})


def bookingdata(request):
    companies = Booking.objects.all()
    all_fields = [field.name for field in Booking._meta.get_fields()]

    flag = True
    return render(request, 'bookingdata.html', {'company': companies, 'column': all_fields, 'fl': flag})


def invoicedata(request):
    invoices = Invoice.objects.all()
    all_fields = [field.name for field in Invoice._meta.get_fields()]
    del all_fields[0]

    all_fields.insert(4, 'TotalAmount')
    return render(request, 'invoicedata.html', {'invoice': invoices, 'column': all_fields, 'Invoices': Invoice})


def contractdata(request):
    contracts = Contracts.objects.all()
    all_fields = [field.name for field in Contracts._meta.get_fields()]
    del all_fields[0:3]
    return render(request, 'contractdata.html', {'contract': contracts, 'column': all_fields})


def searchcompany(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        searched = Companies.objects.filter(name__icontains=search_id)
        all_fields = [field.name for field in Companies._meta.get_fields()]
        del all_fields[0:4]
        flag = False
        return render(request, 'companydata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchshop(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        searched = Shops.objects.filter(Shop_id__startswith=search_id)
        all_fields = [field.name for field in Shops._meta.get_fields()]
        del all_fields[0]
        flag = False
        return render(request, 'shopdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchslot(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        searched = Slots.objects.filter(Slot_id__startswith=search_id)
        all_fields = [field.name for field in Slots._meta.get_fields()]
        del all_fields[0]
        flag = False
        return render(request, 'slotdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchbooking(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        searched = Slots.objects.filter(Booking_id__startswith=search_id)
        all_fields = [field.name for field in Booking._meta.get_fields()]
        # del all_fields[0]
        flag = False
        return render(request, 'bookingdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchcustomer(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        searched = Customer.objects.filter(firstname__icontains=search_id)
        all_fields = [field.name for field in Customer._meta.get_fields()]
        del all_fields[0]

        flag = False
        return render(request, 'customerdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def generateInvoice(request):
    cid = request.POST.get('textfield', None)
    con = Contracts.objects.get(Contract_id=cid)
    stdate = con.Start_Date
    amt = con.Price
    comp = con.Company_id
    bil_freq = con.Billing_Frequency
    new_inv = Invoice(Invoice_id=150001, Amount=amt, Discount=10, GST=18, Date_issued=date.today(
    ), Date_paid=date.today(), Contract_id=cid, issued_by_id=12000110, issued_to_id=comp)
    new_inv.save()
    return render(request, 'geninvoice.html')
