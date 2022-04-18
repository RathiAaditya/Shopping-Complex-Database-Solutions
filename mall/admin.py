from django.contrib import admin
from .models import Company_contact_no, Customer,Companies,Invoice,Contracts,Shops,Booking,Slots,Services,Bound_by
# Register your models here.

admin.site.register(Customer)
admin.site.register(Companies)
admin.site.register(Company_contact_no)
admin.site.register(Invoice)
admin.site.register(Contracts)
admin.site.register(Shops)
admin.site.register(Booking)
admin.site.register(Slots)
admin.site.register(Services)
admin.site.register(Bound_by)