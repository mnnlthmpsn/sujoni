from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200, null=False, default='Category')

    def __str__(self):
        return self.title

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.CharField(max_length=200, null=False, default='User')
    title = models.CharField(max_length=200, null=False, default='Title')
    pub_date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title