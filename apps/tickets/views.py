from django.urls import reverse
from .models import Ticket, Status
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# Create your views here.
@login_required
def index(request):
    tickets_list = Ticket.objects.all()
    paginator = Paginator(tickets_list, 3)
    page = request.GET.get('page')
    tickets = paginator.get_page(page)
    context = { 
        'tickets': tickets,
        'current_url': 'tickets'
    }
    return render(request, "tickets/index.html",context)
@login_required
def create(request):
    users = User.objects.all()
    statuses = Status.objects.all()
    context = {
        'users': users,
        'statuses': statuses,
        'current_url': 'tickets'
    }
    return render(request,  "tickets/create.html", context)
@login_required
def store(request):
    try:
        ticket = Ticket()
        ticket.title = request.POST['title']
        ticket.description = request.POST['description']
        ticket.client = request.POST['client']
        ticket.user_id = request.POST['user_id']
        ticket.status_id = request.POST['status_id']
        ticket.save()
        return HttpResponseRedirect(reverse('tickets:index'))
    except:
        users = User.objects.all()
        statuses = Status.objects.all()
        context = {
            'users': users,
            'statuses': statuses,
            'error_message': 'Error creating the ticket',
            'current_url': 'tickets'
        }
        return render(request,  "tickets/create.html", context)
@login_required
def details(request, id):
    ticket = get_object_or_404(Ticket, pk = id)
    users = User.objects.all()
    statuses = Status.objects.all()
    context = {
        'ticket': ticket,
        'users': users,
        'statuses': statuses,
        'current_url': 'tickets'
    }
    return render(request,  "tickets/details.html", context)
@login_required
def update(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    try:
        ticket.title = request.POST['title']
        ticket.description = request.POST['description']
        ticket.client = request.POST['client']
        ticket.user_id = request.POST['user_id']
        ticket.status_id = request.POST['status_id']
        ticket.save()
        return HttpResponseRedirect(reverse('tickets:index'))
    except:
        users = User.objects.all()
        statuses = Status.objects.all()
        context = {
            'ticket': ticket,
            'users': users,
            'statuses': statuses,
            'error_message': "Error updating the ticket",
            'current_url': 'tickets'
        }
        return render(request,  "tickets/details.html", context)
@require_http_methods(['GET'])
def get_statuses(request):
    statuses = Status.objects.all()
    context = {
        "statuses": statuses,
        'current_url': 'statuses'
    }
    return render(request, 'tickets/statuses/index.html', context)
@require_http_methods(['GET','POST'])
def add_status(request):
    if request.method == 'POST':
        #try:
        status = Status()
        status.title = request.POST['title']
        status.save()
        return HttpResponseRedirect(reverse('tickets:statuses'))
        #except:
        return render(request, 'tickets/statuses/create.html', {"error_message": "The status was not created",'current_url': 'statuses'})
    else:
        return render(request, 'tickets/statuses/create.html', {'current_url': 'statuses'})