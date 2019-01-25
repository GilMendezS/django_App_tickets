from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    deleted_at = models.DateTimeField(nullable = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Status(BaseModel):
    status = mdoels.CharField(max_length=100, unique= true)
    

class Ticket(BaseModel):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    client = models.CharField(max_length = 100, nullable = False)
    user_id = models.ForeignKey(User)
    status_id = models.ForeignKey(Status)
