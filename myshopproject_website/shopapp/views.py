from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from cart.cart import Cart

from .models import *
from .forms import ContactForm, CustomerForm
from .guest_utils import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def home_page(request):
    items = Product.objects.all()
    categories = Category.objects.all()

    if request.method == "POST" and request.POST.get('category_id'):
        items = Product.objects.filter(category=request.POST.get('category_id'))
    else:
        items = Product.objects.all()

    context1 = {
        'categories': Category.objects.all(),
        'items': items
    }

    return render(request, 'shopapp/index.html', context1)


# Views for Card

@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'shopapp/cart_detail.html')




# Views for registration
def registration_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomerForm()
        if request.method == "POST":
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for "+ user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'shopapp/login.html', context)
# Views for login
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or password is not correct")

        context = {}
    
        return render(request, 'shopapp/login.html', context)
# Views for logout
def logout_user(request):
    logout(request)
    return redirect('login')

#  Views for Comment
def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'form':form}
    return render(request, 'shopapp/index.html', context)

