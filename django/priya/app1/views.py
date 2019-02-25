from django.shortcuts import render,redirect
from .forms import RegForm,Login,ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')


def regform(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.Please enter username and password!')
            return redirect('login1')
    else:
        form = RegForm()
    return render(request, 'regform.html', {'form': form})

def login1(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = Login()
    return render(request,'login.html',{'form': form})


def index(request):
    return render(request,'index.html')

@login_required
def courses(request):
       return render(request, 'courses.html')
@login_required
def about(request):
       return render(request, 'about.html')

@login_required
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})







def response(request):

    pta = Regform1.objects.filter(email_id = 'pawanacharya1979@gmail.com')
    formdata = {
        'data': pta
    }
    return render(request, 'response.html', formdata)