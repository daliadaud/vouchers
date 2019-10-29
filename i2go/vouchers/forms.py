from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Voucher


class VoucherForm(forms.Form):
    code = forms.CharField(required=True)

    def clean_code(self):
        if not Voucher.get_voucher(self.cleaned_data['code']):
            raise forms.ValidationError(_("Invalid Code"))
        return self.cleaned_data['code']
