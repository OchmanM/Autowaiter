from django.forms import ModelForm
from django import forms
from .models import Order, Product, Table

class OrderForm(ModelForm):
    PAYMENT_OPTIONS = (
        ('PAYPAL',  'Paypal'),
        ('CASH',    'Cash'),
        ('CARD',    'Card')
    )
    ORDER_STATUS = (
        ('ORDERED',     'Ordered'),
        ('PREPARING',   'Preparing'),
        ('SERVED',      'Served'),
        ('PAYMENT',     'Waiting for payment'),
        ('PAID',        'Paid'),
    )
    order_status = forms.TypedChoiceField(required=False, choices=ORDER_STATUS, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=PAYMENT_OPTIONS)
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active='1'), empty_label='')
    opened_at = forms.DateField(required=False)
    quantity = forms.IntegerField(initial=1)

    class Meta:
        model = Order
        fields = ['product_id','payment_option','quantity','order_status', 'tableFK']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_details','price']


class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['number']