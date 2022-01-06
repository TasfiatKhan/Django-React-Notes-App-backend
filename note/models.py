from django.db import models
from users.models import User
from django.conf import settings 
# Create your models here.


class Tag(models.Model):
    
    tag_name = models.CharField(max_length=25, null=True, blank=True)
    
    def __str__(self):
        return self.tag_name



class Note(models.Model):
    
    tag = models.ManyToManyField(Tag)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body[0:35]