from django.contrib import admin

from .models import Booking, Bound_by, Companies, Company_contact_no, Contracts, Customer, Invoice, Provides, Services, Shops, Slots,ParkingReceipt


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
admin.site.register(Provides)
admin.site.register(ParkingReceipt)


