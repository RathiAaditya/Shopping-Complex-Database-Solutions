from django.http import HttpResponse
from django.shortcuts import render

from mall.models import Customer

# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'User'})


def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1)+int(val2)
    return render(request, "answer.html", {'name': 'User', 'result': res})


def login(request):
    cust1 = Customer()
    cust1.firstname = "Aaditya"
    cust1.lastname = "Rathi"
    cust1.mobile = 8767632011
    cust1.Vaccination_Status = True
    cust1.Vehicle_id = 1234

    cust2 = Customer()
    cust2.firstname = "Milind"
    cust2.lastname = "Jain"
    cust2.mobile = 7379077707
    cust2.Vaccination_Status = False
    cust2.Vehicle_id = 2345

    cust3 = Customer()
    cust3.firstname = "Rohan"
    cust3.lastname = "Gujral"
    cust3.mobile = 8767632013
    cust3.Vaccination_Status = True
    cust3.Vehicle_id = 3456

    custs = [cust1, cust2, cust3]
    return render(request, 'login.html', {'customers': custs})