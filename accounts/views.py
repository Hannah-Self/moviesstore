from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def logout(request): 
    auth_logout(request)
    return redirect('home.index')
#logs user out
#only authenticated users can logout only

@login_required
def orders(request): 
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html', {'template_data': template_data})
#foreignkey relationship bt User model and Order model

def login(request): 
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None: 
            template_data['error'] = 'The Username or Password is incorrect.'
            return render(request, 'accounts/login.html', {'template_date': template_data})
        else: 
            auth_login(request, user)
            return redirect('home.index')
#(above) see if login exists, send accordingly
def signup(request): 
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})
    #imported UserCreationForm (built-in)
    #created template_data var with title
    #check if curr HTTP request is GET, if GET, means it will be nav to another
    #rendered acc/signup.html tempalte
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else: 
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})
    #import redirect
    #for POST, create user
    #if valid, goes thru
    #saves if valid, takes to homem
    #else --> pass and refresh
# Create your views here.

#user --> deda
#pass --> iLoveFrontEnd12
