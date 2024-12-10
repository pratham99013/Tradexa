from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from project.models import User, Product, Order

def display_tables(request):
    users = User.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'hello.html', {
        'users': users,
        'products': products,
        'orders': orders,
    })
