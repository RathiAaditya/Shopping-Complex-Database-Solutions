from tkinter import Widget
from django import forms
from .models import Booking, Bound_by, Companies, Company_contact_no, Contracts, Customer, Services, Shops, Slots, Provides
# from crispy_forms.helper
# from bootstrap_datepicker_plus import DatePickerInput


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ["Company_id", "name", "email"]
        labels = {"Company_id": "Company ID",
                  'name': "Company Name", "email": "Company Email"}


class CompanyContactFrom(forms.ModelForm):
    class Meta:
        model = Company_contact_no
        fields = ["Contact_no"]


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shops
        fields = '__all__'


class SlotForm(forms.ModelForm):
    class Meta:
        model = Slots
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


class ProvidesForm(forms.ModelForm):
    class Meta:
        model = Provides
        fields = ["Service"]


class Bound_byForm(forms.ModelForm):
    class Meta:
        model = Bound_by
        fields = '__all__'


class DateForm(forms.Form):
    date = forms.DateField(
        input_formats=['%j %M %Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))


class DateForm(forms.Form):
    date = forms.DateField(
        input_formats=['%j %M %Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        }))


class DateForm(forms.Form):
    date = forms.DateField(
        input_formats=['%j %M %Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker3'
        }))
