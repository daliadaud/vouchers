from django.shortcuts import render

from .forms import VoucherForm
from .models import Voucher
# Create your views here.

def use_voucher(request):

    if request.method == "POST":
        form = VoucherForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            voucher = Voucher.get_voucher(code)
            voucher.use_voucher()

            return render(request, 'voucher.html', {'form': form, 'voucher': voucher})
        return render(request, 'voucher.html', {'form': form})
    else:
        form = VoucherForm()
        return render(request, 'voucher.html', {'form': form})
