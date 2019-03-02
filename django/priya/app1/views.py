from django.shortcuts import render,redirect
from .forms import RegForm,Login,ContactForm,AssignmentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from .models import Assignment1,Assignment
from django.core.mail import EmailMessage

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
            name = form.cleaned_data.get('Name')
            email = form.cleaned_data.get('Email')
            unit = form.cleaned_data.get('Unit')
            subject = form.cleaned_data.get('Subject')
            body = {'Name':name,'Email':email,'Unit':unit,'Subject':subject},

            email = EmailMessage(
                'Contact From',
                str(body),
                to=['pawanacharya1979@gmail.com']
            )
            email.send()
            messages.success(request, 'Thank You! for contacting us, we will get back to you soon.')
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})

@login_required
def assignment(request):
    if request.method == 'POST' and request.FILES['myfile']:
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('TraineeName')
            assignmentname = form.cleaned_data.get('AssignmentName')
            course = form.cleaned_data.get('CourseName')
            body = {'Name': name, 'AssignmentName': assignmentname ,'Unit': course},

            email = EmailMessage(
                'Assignment Form',
                str(body),
                to=['pawanacharya1979@gmail.com']
            )
            email.send()
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)
            messages.success(request, 'Successfully Uploaded! Admin will review the task. Thank You!')
        return HttpResponseRedirect('/assignments/')
    else:
        form = AssignmentForm()
        #info2 = request.user
        #email = info2.email
        info = Assignment.objects.filter(Email=request.user.email)
    return render(request, 'assignment.html', {'form': form, 'details': info})

