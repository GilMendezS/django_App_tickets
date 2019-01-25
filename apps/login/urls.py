from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('authenticate', views.try_login, name='authenticate'),
    path('logout', views.logout, name='logout')
]