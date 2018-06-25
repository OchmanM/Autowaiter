from django.shortcuts import render, redirect
from .models import Order, Product, Table
from .forms import OrderForm, ProductForm, TableForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
import json
from django.contrib.auth.models import User


@login_required
def index(request):
    orders = Order.objects.all()
    return render(request, 'index.html', {'orders': orders})

@login_required
def show(request, order_id):
    with transaction.atomic():
        order = Order.objects.filter(id=order_id)
        return render(request, 'show.html', {'order': order})

@login_required
def new(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new.html', {'form':form})

@login_required
def edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm(instance=order)
        return render(request, 'edit.html', {'form':form})


@login_required
def destroy(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/', messages.success(request, 'Order was successfully deleted.', 'alert-success'))



#Product

@login_required
def index_product(request):
    products = Product.objects.filter(active='1')
    return render(request, 'index_product.html', {'products': products})    

@login_required
def new_product(request):
    transaction.set_autocommit(False)
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            transaction.set_autocommit(True)
            if form.save():
                return redirect('/products', messages.success(request, 'Product was successfully created.', 'alert-success'))
            else:
                return redirect('/products', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/products', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        product_form = ProductForm()
        return render(request, 'new_product.html', {'product_form':product_form})    

@login_required
def destroy_product(request, product_id):
    if Product.objects.filter(id=product_id).update(active='0'):
        return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))  
    else:
        return redirect('/products', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger'))

@login_required
def index_table(request):
    tables = Table.objects.all()
    return render(request, 'index_table.html', {'tables': tables})

@login_required
def new_table(request):
    if request.POST:
        form = TableForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/tables',
                                messages.success(request, 'Table was successfully created.', 'alert-success'))
            else:
                return redirect('/tables', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/tables', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        table_form = TableForm()
        return render(request, 'new_table.html', {'table_form': table_form})

@login_required
def destroy_table(request, table_id):
    if Table.objects.filter(id=table_id).update(active='0'):
        return redirect('/tables',
                        messages.success(request, 'Product was successfully deleted.', 'alert-success'))
    else:
        return redirect('/tables',
                        messages.error(request, 'Cannot delete product while its order exists.', 'alert-danger'))

@login_required
def status_change(request, order_id):
    ORDER_STATUS = {'ORDERED':'PREPARING',
                    'PREPARING':'SERVED',
                    'SERVED':'PAYMENT',
                    'PAYMENT':'PAID'}
    obj = Order.objects.get(pk=order_id)
    if obj.order_status == 'PAID':
        return redirect('/',
                        messages.error(request, "Order couldn't be changed.", 'alert-danger'))
    else:
        obj.order_status = ORDER_STATUS.get(obj.order_status)
        obj.save()
        return redirect('/', messages.success(request, 'Order status changed.', 'alert-success'))