from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
       
class Status(models.Model):
    title = models.CharField(max_length=100, unique= True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null = True)
    def __str__(self):
        return self.title
class Ticket(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    client = models.CharField(max_length = 100, blank = True, null = False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null = True)
    def __str__(self):
        return self.title
