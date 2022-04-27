from asyncio.windows_events import NULL
from urllib import response
from django import forms
from django.http import HttpResponse
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from mall.models import Companies, Company_contact_no, Customer, Invoice, Contracts, AdminModel, ParkingReceipt, Provides, Shops, Slots, Services, Booking
from mall.models import Booking, Companies, Customer, Invoice, Contracts, AdminModel, Services, Shops, Slots
from django.shortcuts import render

from mall.models import Companies, Customer, Invoice, Contracts
from .forms import CompanyForm, CompanyContactFrom, CustomerForm, ContractForm, ServicesForm, ProvidesForm, ShopForm, SlotForm
#import forms


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
    del all_fields[0:2]
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
    del all_fields[0]
    all_fields[3] = 'First Name'
    flag = True
    return render(request, 'bookingdata.html', {'booking': booking, 'column': all_fields, 'fl': flag})


def invoicedata(request):
    invoices = Invoice.objects.all()
    all_fields = [field.name for field in Invoice._meta.get_fields()]
    # del all_fields[0]
    del all_fields[2:4]
    flag = True
    all_fields.insert(2, 'TotalAmount')
    return render(request, 'invoicedata.html', {'invoice': invoices, 'column': all_fields, 'Invoices': Invoice, 'fl': flag})


def searchinvoice(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        temp = Companies.objects.filter(name__icontains=search_id)
        updated_search_id = []
        for i in temp:
            updated_search_id.append(i.Company_id)
        filterfields = Q()
        for u in updated_search_id:
            filterfields = filterfields | Q(issued_by_id=u) | Q(issued_to_id=u)
        print(len(filterfields))
        filflag = False
        if(len(filterfields) == 0):
            filflag = True
        searched = Invoice.objects.filter(filterfields)
        all_fields = [field.name for field in Invoice._meta.get_fields()]
        del all_fields[0]
        del all_fields[2:4]
        all_fields.insert(2, 'TotalAmount')
        flag = False
        return render(request, 'invoicedata.html', {'search': searched, 'column': all_fields, 'fl': flag, 'ffl': filflag})


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
        filflag = False
        if(len(searched) == 0):
            filflag = True
            return render(request, 'companydata.html', {'ffl': filflag})
        all_fields = [field.name for field in Companies._meta.get_fields()]
        del all_fields[0:4]
        flag = False
        return render(request, 'companydata.html', {'search': searched, 'column': all_fields, 'fl': flag, 'ffl': filflag})


def searchshop(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)

        filterfields = Q(Shop_id__iexact=search_id) | Q(
            Status__icontains=search_id)
        searched = Shops.objects.filter(filterfields)
        all_fields = [field.name for field in Shops._meta.get_fields()]
        del all_fields[0]
        flag = False
        return render(request, 'shopdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchservice(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        filterfields = Q(Service_id__iexact=search_id) | Q(
            Type__icontains=search_id)
        searched = Services.objects.filter(filterfields)
        all_fields = [field.name for field in Shops._meta.get_fields()]
        del all_fields[0]
        flag = False
        return render(request, 'servicedata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchslot(request):

    if request.method == 'POST':
        # a = 2

        search_id = request.POST.get('textfield', None)

        if search_id == True:
            search_id = 1
        if search_id == False:
            search_id = 0

        filterfields = Q(Slot_status__iexact=search_id) | Q(
            Slot_id__iexact=search_id)
        searched = Slots.objects.filter(filterfields)
        all_fields = [field.name for field in Slots._meta.get_fields()]
        del all_fields[0]
        flag = False
        return render(request, 'slotdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchbooking(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        searched = Booking.objects.filter(Booking_id=search_id)
        filterfields = Q(Booking_id__icontains=search_id) | Q(
            mobile_id__istartswith=search_id) | Q(Slot__istartswith=search_id)
        all_fields = [field.name for field in Booking._meta.get_fields()]
        del all_fields[0]
        all_fields[3] = 'First Name'
        # del all_fields[0]
        flag = False
        return render(request, 'bookingdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def searchcustomer(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        filterfields = Q(firstname__icontains=search_id) | Q(
            lastname__icontains=search_id) | Q(mobile_id__icontains=search_id) | Q(Vehicle_id__icontains=search_id)
        searched = Customer.objects.filter(filterfields)
        all_fields = [field.name for field in Customer._meta.get_fields()]
        del all_fields[0]

        flag = False
        return render(request, 'customerdata.html', {'search': searched, 'column': all_fields, 'fl': flag})


def generateInvoice(request):
    flg = False
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
    return render(request, 'geninvoice.html', {'fl': flag, 'f': flg})
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
    # cid = request.POST.get('textfield', None)
    # con = Contracts.objects.get(Contract_id=cid)
    # stdate = con.Start_Date
    # amt = con.Price
    # comp = con.Company_id
    # bil_freq = con.Billing_Frequency
    # new_inv = Invoice(Invoice_id=150001, Amount=amt, Discount=10, GST=18, Date_issued=date.today(
    # ), Date_paid=date.today(), Contract_id=cid, issued_by_id=12000110, issued_to_id=comp)
    # new_inv.save()
    # return render(request, 'geninvoice.html')


def generateBooking(request):
    flg = True
    flag = True
    receipts = Booking.objects.all()
    for i in receipts:
        amt = i.Slot.Rate
        dati = i.in_time.date()
        bid = i.Booking_id
        slid = i.Slot_id
        new_rept = ParkingReceipt(
            Amount=amt, Date_of_issue=dati, Booking_id=bid, Slot_id=slid)
        new_rept.save()
    return render(request, 'geninvoice.html', {'f': flg, 'fl': flag})


def receiptdata(request):
    recpts = ParkingReceipt.objects.all()
    all_fields = [field.name for field in ParkingReceipt._meta.get_fields()]
    all_fields.append('First Name')
    #del all_fields[0]
    flag = True
    return render(request, 'receiptdata.html', {'recpt': recpts, 'column': all_fields, 'fl': flag})


def Companyform(request):
    if request.method == "POST":
        form01 = CompanyForm(request.POST)
        form02 = CompanyContactFrom(request.POST)
        if form01.is_valid():
            a = form01.save()
            b = form02.save(commit=False)
            print("saved")
            if form02.is_valid():
                b = form02.save(commit=False)
                b.Company = a
                b.save()
                form02.save_m2m()
                return redirect('/')
    else:
        form01 = CompanyForm()
        form02 = CompanyContactFrom()
    context = {'form01': form01, 'form02': form02, }
    return render(request, 'companyinput.html', context)


def Contractform(request):
    if request.method == "POST":
        form1 = ContractForm(request.POST)
        form2 = ProvidesForm(request.POST)
        print("saved")
        if form1.is_valid():
            a = form1.save()
            b = form2.save(commit=False)
            print("saved")
            if form2.is_valid() and a.Type == "T":
                b = form2.save(commit=False)
                b.Contract = a
                b.save()
                form2.save_m2m()
                return redirect('home/form/insertContract')
            return redirect('home/form/insertContract')
    else:
        form1 = ContractForm()
        form2 = ProvidesForm()
    context1 = {'form1': form1, 'form2': form2, }
    return render(request, 'contractinput.html', context1)


def Shopform(request):
    if request.method == "POST":
        form3 = ShopForm(request.POST)
        if form3.is_valid():
            a = form3.save()
            return redirect('/form/insertShop')
    else:
        form3 = ShopForm()
    context2 = {'form3': form3}
    return render(request, 'shopinput.html', context2)


def Slotform(request):
    if request.method == "POST":
        form4 = SlotForm(request.POST)
        if form4.is_valid():
            a = form4.save()
            return redirect('/form/insertSlot')
    else:
        form4 = SlotForm()
    context3 = {'form4': form4}
    return render(request, 'slotinput.html', context3)


def Servicesform(request):
    if request.method == "POST":
        form5 = ServicesForm(request.POST)
        if form5.is_valid():
            a = form5.save()
            return redirect('/form/insertServices')
    else:
        form5 = ServicesForm()
    context4 = {'form5': form5}
    return render(request, 'servicesinput.html', context4)


def Customerform(request):
    if request.method == "POST":
        form6 = CustomerForm(request.POST)
        if form6.is_valid():
            a = form6.save()
            return redirect('/form/insertCustomer')
    else:
        form6 = CustomerForm()
    context5 = {'form6': form6}
    return render(request, 'customerinput.html', context5)
