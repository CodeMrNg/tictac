from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from threading import Thread



# Create your views here.
def index(request):
    return render(request, 'landing.html')

@login_required
def dash(request):
    user = request.user
    event = Event.objects.filter(user=user).order_by('-pk')
    context = {
        'events': event,
    }
    return render(request, 'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = AllUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AllUserCreationForm()
    return render(request, 'register.html', {'form': form})

def loginn(request):
    message=''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = messages.success(request, 'Vous êtes connecté.')
                return redirect('dash')
            else:
                message = messages.error(request, 'Identifiants invalides.')
    return render(
        request, 'login.html', context={'form': form, 'message': message})

def logoutt(request):
    logout(request)
    return redirect('home')

@login_required
def addevent(request):
    user=request.user
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, user=user)
        if form.is_valid():
            event = form.save()
            return redirect('dash')
    else:
        form = EventForm(user=request.user)
    return render(request, 'addevent.html', {'form': form})



def new_ticket(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            ticket = Ticket.objects.get(pk=form.instance.id)
            return redirect(f'/accounts/success/{ticket.id}')
    else:
        form = TicketForm()

    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'new_ticket.html', {'form': form, 'event':event, 'host_name': request.get_host(),})
    
def success(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    return render(request, 'success.html', {'ticket': ticket, 'host_name': request.get_host(),})

@login_required
def ticket_detail(request, ticket_id):
    user = request.user
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    event = Event.objects.filter(user=user.id)
    
    if request.method == 'POST':
        form = QuantForm(request.POST)
        if form.is_valid():
            quant = form.cleaned_data['quant']

            ticket.quantite -= int(quant)
            ticket.save()
            return redirect('ticket', ticket_id=ticket.id)
    else:
        form = QuantForm()
        
    return render(request, 'ticket_detail.html', {'ticket': ticket, 'event': event, 'form': form})