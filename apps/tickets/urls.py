from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:id>/details', views.details, name = 'details'),
    path('add', views.store , name='store'),
    path('create', views.create, name='create'),
    path('<int:id>/update', views.update, name='update'),
    path('statuses', views.get_statuses, name='statuses'),
    path('statuses/add', views.add_status, name='add-status')
]
