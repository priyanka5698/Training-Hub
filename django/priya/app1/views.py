from django.shortcuts import render,redirect
from .forms import RegForm,Login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')


def regform(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
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




def response(request):

    pta = Regform1.objects.filter(email_id = 'pawanacharya1979@gmail.com')
    formdata = {
        'data': pta
    }
    return render(request, 'response.html', formdata)