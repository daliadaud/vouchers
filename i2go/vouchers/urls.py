from django.urls import path

from . import views
app_name = 'vouchers'


urlpatterns = [

    path('', views.use_voucher, name='use_voucher'),
    ]