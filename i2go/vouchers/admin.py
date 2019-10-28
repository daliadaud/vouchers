from django.contrib import admin

from .models import Voucher

class VoucherAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'value_type', 'value', 'usage_remainder']



admin.site.register(Voucher, VoucherAdmin)