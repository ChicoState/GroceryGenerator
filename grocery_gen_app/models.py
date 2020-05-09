from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_lists(models.Model):
	list_name = models.CharField(max_length=30)
	list_owner = models.ForeignKey(User, on_delete=models.CASCADE)
