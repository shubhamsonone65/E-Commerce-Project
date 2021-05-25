from django.contrib import admin
from .models import contact,customer,product,order

# Register your models here.
admin.site.register(contact),
admin.site.register(customer),
# admin.site.register(product),
admin.site.register(order),

@admin.register(product)
class productmodel(admin.ModelAdmin):
    list_filter=('cat','subcat')