from django import forms
from .models import Order, Customer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'quantity', 'status']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number']