from django.shortcuts import render
from .models import Ticket
# Create your views here.
def index(request):
    tickets = Ticket.objects.all()
    context = { 
        'tickets': tickets
    }
    return render(request, "tickets/index.html",context)
