
from datetime import date
import datetime
from tkinter import CASCADE
from xmlrpc.client import boolean
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Customer(models.Model):
    mobile_id = models.BigIntegerField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    Vaccination_Status = models.BooleanField(default=False)
    Vehicle_id = models.CharField(max_length=30)


class Companies(models.Model):
    Company_id = models.CharField(primary_key=True, max_length=40)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = "Comp"


class Company_contact_no(models.Model):
    Contact_no = models.CharField(validators=[RegexValidator(
        regex='^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$', message='should be a valid phone number', code='no match')], max_length=12)

    Company = models.ForeignKey(Companies,on_delete=models.CASCADE,primary_key=True,default='def')


    class Meta:
        unique_together = (("Contact_no", "Company_id"),)


class Contracts(models.Model):
    Type_choices = [
        ('S','Selling'),
        ('R','Renting')
    ]
    Contract_id = models.CharField(max_length=40, primary_key=True)
    Type = models.CharField(max_length=1, choices=Type_choices)
    Price = models.FloatField()
    Start_Date = models.DateTimeField(auto_now_add=True)
    End_Date = models.DateTimeField(auto_now_add=True)
    # Signing_Date = date = models.DateField(
    #     _Feature("Date"), default=date.today)
    Signing_Date = models.DateField(auto_now_add=True)
    Billing_Frequency = models.IntegerField()
    Company = models.ForeignKey(Companies,on_delete=models.CASCADE, default='def')

    class Meta:
        verbose_name_plural = "cid"

class Contracts(models.Model):
    Type_choices = [
        ('S','Selling'),
        ('R','Renting'),
    ]
    Contract_id = models.CharField(max_length=40, primary_key=True)
    Type = models.CharField(max_length =1, choices= Type_choices)
    Price = models.FloatField()
    Start_Date = models.DateTimeField(auto_now_add=True)
    End_Date = models.DateTimeField(auto_now_add=True)


    Signing_Date = models.DateField(auto_now_add=True)
    Billing_Frequency = models.IntegerField()
   

    class Meta:
        verbose_name_plural = "cid"

    Company = models.ForeignKey(
        Companies, default=None, on_delete=models.CASCADE)

class Invoice(models.Model):
    Invoice_id = models.CharField(max_length=50, primary_key=True)
    Amount = models.FloatField()
    Discount = models.FloatField()
    GST = models.FloatField()
    Date_issued = models.DateTimeField(auto_now_add=True)
    Date_paid = models.DateTimeField(auto_now=True)

    Contract = models.ForeignKey(Contracts,on_delete=models.CASCADE,default='def')
    issued_by = models.ForeignKey(Companies,on_delete=models.CASCADE, related_name='company_issuing',default='def')
    issued_to = models.ForeignKey(Companies,on_delete=models.CASCADE, related_name='company_issued',default='def')

    





class Shops(models.Model):
    Status_choices = [
        ('S','Sold'),
        ('R','Rented'),

        ('E','Empty')
    ]
    Shop_id = models.CharField(max_length=40, primary_key=True)
    Status = models.CharField(max_length=1,choices=Status_choices,default='E')


class Slots(models.Model):
    Slot_id = models.IntegerField(primary_key=True)
    Slot_status = models.BooleanField(default=False)
    Rate = models.FloatField()

    class Meta:
        verbose_name = "slots"


class Booking(models.Model):
    Booking_id = models.CharField(max_length=40, primary_key=True)
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(auto_now_add=True)

    mobile = models.ForeignKey(Customer, on_delete=models.CASCADE,validators=[RegexValidator(
        regex='^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$', message='should be a valid phone number', code='no match')])
    Invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,default=0)
    Slot = models.ForeignKey(Slots,on_delete=models.CASCADE,default='def' )



    


class Services(models.Model):
    Service_id = models.CharField(primary_key=True, max_length=40)
    Type = models.CharField(max_length=10)


class Provides(models.Model):

    Contract = models.ForeignKey(Contracts,on_delete=models.CASCADE, primary_key=True,default='def')
    Service = models.ForeignKey(Services,on_delete=models.CASCADE,default='def')


    class Meta:
        unique_together = (("Contract_id", "Service_id"),)

    


class Bound_by(models.Model):

    Contract = models.ForeignKey(Contracts,on_delete=models.CASCADE, primary_key=True,default='def')
    Shop = models.ForeignKey(Shops,on_delete=models.CASCADE,default='def')

    class Meta:
        unique_together = (("Contract_id", "Shop_id"),)

    