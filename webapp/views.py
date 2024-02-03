from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .forms import OrderForm, CustomerForm

# Create your views here.
def home_page(request):
	return render(request, 'pages/home.html')


def login_page(request):
	return HttpResponse("log in")


def order_page(request):
    products = Product.objects.all()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
          
            return redirect('Homepage')
    else:
        form = OrderForm()

    return render(request, 'pages/order.html', {'products': products, 'form': form})

def customer_creation_page(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            # You can customize the redirect or response here
            return redirect('ordering_page')
    else:
        form = CustomerForm()

    return render(request, 'pages/create_customer.html', {'form': form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'pages/orderlist.html', {'orders': orders})

def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = OrderForm(request.POST or None, instance=order)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('order_list')

    context = {'form': form, 'product': order}
    return render(request, 'pages/update_order.html', context)

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    context = {'product': order}
    return render(request, 'pages/delete_order.html', context)