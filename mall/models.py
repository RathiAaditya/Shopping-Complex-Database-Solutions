from xmlrpc.client import boolean
from django.db import models

# Create your models here.


class Customer:
    mobile_no: int
    firstname: str
    lastname: str
    Vaccination_Status: boolean
    Vehicle_id: str
