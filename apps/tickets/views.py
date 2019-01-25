from django.urls import reverse
from .models import Ticket, Status
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# Create your views here.
def index(request):
    tickets = Ticket.objects.all()
    context = { 
        'tickets': tickets
    }
    return render(request, "tickets/index.html",context)
def details(request, id):
    ticket = get_object_or_404(Ticket, pk = id)
    users = User.objects.all()
    statuses = Status.objects.all()
    context = {
        'ticket': ticket,
        'users': users,
        'statuses': statuses
    }
    return render(request,  "tickets/details.html", context)
def update(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    try:
        ticket.title = request.POST['title']
        ticket.description = request.POST['description']
        ticket.client = request.POST['client']
        ticket.user_id = User.objects.get(pk=request.POST['user_id'])
        ticket.status_id = Status.objects.get(pk=request.POST['status_id'])
        ticket.save()
        return HttpResponseRedirect(reverse('tickets:index'))
    except:
        users = User.objects.all()
        statuses = Status.objects.all()
        context = {
            'ticket': ticket,
            'users': users,
            'statuses': statuses,
            'error_message': "Error updating the ticket"
        }
        return render(request,  "tickets/details.html", context)
        