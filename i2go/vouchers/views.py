from django.shortcuts import render

from .forms import VoucherForm
from .models import Voucher
# Create your views here.

def use_voucher(request):

    if request.method == "GET":
        form = VoucherForm()
        return render(request, 'voucher.html', {'form': form})

    elif request.method == "POST":
        success = "yes"
        form = VoucherForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            voucher = Voucher.get_voucher(code)
            if not voucher:
                success = "false"
            else:
                voucher.use_voucher()

    return render(request, 'voucher.html', {'form': form, 'voucher': voucher, 'success': success})
