from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:id>/details', views.details, name = 'details'),
    path('<int:id>/update', views.update, name='update')
    
]
