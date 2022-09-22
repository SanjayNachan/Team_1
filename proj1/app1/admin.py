from django.contrib import admin
from .models import Customer,CustomerInvoice,CustomerOrder,BalanceSheet,VendorInvoice,Vendor,Product,PurchaseOrder,Category,GST,Discount
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerInvoice)
admin.site.register(CustomerOrder)
admin.site.register(BalanceSheet)
admin.site.register(Vendor)
admin.site.register(VendorInvoice)
admin.site.register(Product)
admin.site.register(PurchaseOrder)
admin.site.register(Category)
admin.site.register(GST)
admin.site.register(Discount)
