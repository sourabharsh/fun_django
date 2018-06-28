from django.shortcuts import render, redirect
from  .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.forms   import AuthenticationForm

# Create your views here.


def HomePage(request):
    template_name = "home/index.html"
    forms = {
            "signup_form" : SignUpForm(request.POST),
            "login_form"  : AuthenticationForm(request.POST)
        }
    
    return render(request, template_name, {'forms': forms})


def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            print(username, raw_password)
            user = authenticate(username=username, password= raw_password)
            login(request, user)
            return redirect("home")
        
def logout_view(request):
    logout(request)
    return redirect("home")

def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(data= request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            raw_password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return HttpResponseRedirect("home")
        else:
            return HttpResponseRedirect("home")
    
