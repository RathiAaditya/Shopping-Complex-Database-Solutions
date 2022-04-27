from asyncio.windows_events import NULL
from urllib import response
from django.http import HttpResponse
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from mall.models import Companies, Company_contact_no, Customer, Invoice, Contracts, AdminModel, Provides, Shops, Slots, Services, Booking

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


def otp(request):
    return render(request, 'otp.html')


def customerdata(request):
    customers = Customer.objects.all()
    all_fields = [field.name for field in Customer._meta.get_fields()]
    del all_fields[0]
    flag = True
    return render(request, 'customerdata.html', {'customer': customers, 'column': all_fields, 'fl': flag})


def servicedata(request):
    service = Services.objects.all()
    all_fields = [field.name for field in Services._meta.get_fields()]
    del all_fields[0]
    flag = True
    return render(request, 'servicedata.html', {'services': service, 'column': all_fields, 'fl': flag})


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
    l = []
    for i in companies:
        l.append(Company_contact_no.objects.filter(Company_id=i.Company_id))
    zipped_data = zip(companies, l)
    all_fields = [field.name for field in Companies._meta.get_fields()]
    del all_fields[0:4]
    all_fields.append('Contact_nos')
    flag = True
    return render(request, 'companydata.html', {'zip': zipped_data, 'column': all_fields, 'fl': flag})


def bookingdata(request):
    booking = Booking.objects.all()
    all_fields = [field.name for field in Booking._meta.get_fields()]

    flag = True
    return render(request, 'bookingdata.html', {'booking': booking, 'column': all_fields, 'fl': flag})


def invoicedata(request):
    invoices = Invoice.objects.all()
    all_fields = [field.name for field in Invoice._meta.get_fields()]
    del all_fields[0]
    del all_fields[2:4]
    flag = True
    all_fields.insert(2, 'TotalAmount')
    return render(request, 'invoicedata.html', {'invoice': invoices, 'column': all_fields, 'Invoices': Invoice, 'fl':flag})

def searchinvoice(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        temp = Companies.objects.filter(name__icontains=search_id)
        updated_search_id = []
        for i in temp:
            updated_search_id.append(i.Company_id)
        print(updated_search_id)
        filterfields = Q()
        for u in updated_search_id:
            filterfields = filterfields | Q(issued_by_id=u) | Q(issued_to_id=u)
        print(filterfields) 
        searched = Invoice.objects.filter(filterfields)
        print(searched)
        all_fields = [field.name for field in Invoice._meta.get_fields()]
        del all_fields[0]
        del all_fields[2:4]
        all_fields.insert(2, 'TotalAmount')
        flag = False
        return render(request, 'invoicedata.html', {'search': searched, 'column': all_fields, 'fl': flag})

def contractdata(request):
    contracts = Contracts.objects.all()
    all_fields = [field.name for field in Contracts._meta.get_fields()]
    del all_fields[0:3]
    return render(request, 'contractdata.html', {'contract': contracts, 'column': all_fields})


def providesdata(request):
    provides = Provides.objects.all()
    all_fields = [field.name for field in Provides._meta.get_fields()]
    # del all_fields[0:3]
    all_fields.append('Company')
    flag = True
    return render(request, 'providesdata.html', {'provide': provides, 'column': all_fields, 'fl': flag})


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


def searchservice(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        searched = Services.objects.filter(Service_id__startswith=search_id)
        all_fields = [field.name for field in Shops._meta.get_fields()]
        del all_fields[0]
        flag = False
        return render(request, 'servicedata.html', {'search': searched, 'column': all_fields, 'fl': flag})


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
        searched = Booking.objects.filter(Booking_id__startswith=search_id)
        all_fields = [field.name for field in Booking._meta.get_fields()]
        # del all_fields[0]
        flag = False
        return render(request, 'bookingdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchcustomer(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        filterfields = Q(firstname__icontains=search_id) | Q(
            lastname__icontains=search_id) | Q(mobile_id__icontains=search_id)
        searched = Customer.objects.filter(filterfields)
        all_fields = [field.name for field in Customer._meta.get_fields()]
        del all_fields[0]

        flag = False
        return render(request, 'customerdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def generateInvoice(request):
    # cid = request.POST.get('textfield', None)
    objlist = Contracts.objects.filter(Type='T')
    flag = True
    for i in objlist:
        print(i.Contract_id)
        no_of_years = relativedelta(i.End_Date, i.Start_Date).years
        print(no_of_years)
        amt = i.Price
        comp = i.Company_id
        bil_freq = i.Billing_Frequency
        num_of_invoices = int(no_of_years / bil_freq)
        print(num_of_invoices)
        for j in range(num_of_invoices):
            print(j)
            new_inv = Invoice(Amount=amt, Discount=10, GST=18, Date_issued=i.Start_Date+relativedelta(years=j),
                              Date_paid=date.today()+timedelta(4), Contract_id=i.Contract_id, issued_by_id=comp, issued_to_id=100000)
            new_inv.save()
    return render(request, 'geninvoice.html', {'fl': flag})
    # stdate = con.Start_Date
    # amt = con.Price
    # comp = con.Company_id
    # bil_freq = con.Billing_Frequency
    # no_of_days = (date.today() - stdate.date()).days
    # num_of_invoices = int(no_of_days / bil_freq)
    # for i in range(num_of_invoices):
    #     new_inv = Invoice(Amount=amt, Discount=10,GST=18,Date_issued=stdate+timedelta(i*bil_freq),Date_paid=date.today()+timedelta(4),Contract_id=cid, issued_by_id=12000110,issued_to_id=comp)
    #     new_inv.save()
    # except:
    #     flag = False

# def generateInvoice(request):
#     # cid = request.POST.get('textfield', None)
#         objlist = Contracts.objects.filter(Type='R')
#         flag = True
#         for i in objlist:
#             no_of_months = relativedelta(i.End_Date, i.Start_Date).years*12
#             amt = i.Price
#             comp = i.Company_id
#             bil_freq = i.Billing_Frequency
#             num_of_invoices = int(no_of_months/ bil_freq)
#             for j in range(num_of_invoices):
#                 new_inv = Invoice(Amount=amt, Discount=10,GST=18,Date_issued=i.Start_Date+relativedelta(months=j),Date_paid=date.today()+timedelta(4),Contract_id=i.Contract_id, issued_by_id=100000,issued_to_id=comp)
#                 new_inv.save()
