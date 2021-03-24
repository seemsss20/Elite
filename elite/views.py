from django.contrib import messages
from django.shortcuts import render, redirect
# this is my comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
import datetime
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Member
from .filters import MemberFilter


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        time = datetime.datetime.now()

        contact = Contact(name=name, email=email,
                          message=message, subject=subject, Time=time)
        print(contact)
        contact.save()
        messages.success(request, "Your form has been submitted successfully.")

    return render(request, 'booking/contact.html')

# Create your views here.


def allCity(request):
    city = Member.objects.all()

    filter_form = MemberFilter(request.GET, queryset=city)
    city = filter_form.qs
    context = {'city': city, 'filter_form': filter_form}
    return render(request, 'booking/bookflight.html', context)


def index(request):
    context = {}
    return render(request, 'booking/index.html', context)


def Book(request):
    context = {}
    return render(request, 'booking/Book.html', context)


def about(request):
    context = {}
    return render(request, 'booking/about.html', context)


def bookflight(request):
    context = {}
    return render(request, 'booking/bookflight.html', context)

def details(request,id):
    context = {}
    flight = Member.objects.get(Sr_No=id)
    return render(request, 'booking/details.html', {'flight': flight})

def checkout(request):
    context = {}
    return render(request, 'booking/checkout.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account was created for ' + user)

    context = {'form': form}
    return render(request, 'booking/register.html', context)


def destination(request):
    context = {}
    return render(request, 'booking/destination.html', context)


def FAQs(request):
    context = {}
    return render(request, 'booking/FAQs.html', context)


def group(request):
    context = {}
    return render(request, 'booking/group.html', context)


def hotel(request):
    context = {}
    return render(request, 'booking/hotel.html', context)


def login(request):
    context = {}
    return render(request, 'booking/login.html', context)


def quick(request):
    context = {}
    return render(request, 'booking/quick.html', context)


def services(request):
    context = {}
    return render(request, 'booking/services.html', context)


def view(request):
    context = {}
    return render(request, 'booking/view.html', context)
