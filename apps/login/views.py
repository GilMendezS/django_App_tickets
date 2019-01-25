from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(['GET'])
def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tickets:index'))
    return render(request, 'auth/login.html')
@require_http_methods(['POST'])
def try_login(request):
    username = request.POST['username']   
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    error_message = ''
    print("user {}".format(user))
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('tickets:index'))
    else:
        context = {
            "error_message":'Incorrect Login.'
        }
        return render(request, 'auth/login.html', context)
@require_http_methods(['POST'])
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth:login'))