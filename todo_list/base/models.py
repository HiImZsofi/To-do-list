from enum import auto
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #one to many relationship, the user can have more than 1 item and they will be deleted if the user is deleted
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
