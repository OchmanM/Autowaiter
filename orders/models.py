from django.db import models
from django.utils import timezone

# Create your models here.
class Table(models.Model):
    number = models.IntegerField(unique = True, editable=True)
    isFree = models.BooleanField(default = True, editable=True)

    def __str__(self):
        return str(self.number)

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_details = models.TextField()
    price = models.IntegerField()
    active = models.IntegerField(default='1')

    def __str__(self):
        return '%s [%s PLN]' % (self.product_name, self.price)

class Order (models.Model):
    tableFK = models.ForeignKey(Table, related_name = 'orders', on_delete = models.CASCADE, default = 1)
    opened_at =  models.DateTimeField('date_created', default=timezone.now, editable=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_option = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    quantity = models.IntegerField()
    paid = models.BooleanField(default=False)