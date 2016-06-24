from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    taskName = models.CharField(max_length=30)
    taskCompleted = models.BooleanField()
    taskImportance = models.IntegerField(default=1, validators=[MaxValueValidator(3), MinValueValidator(1)])
    creator = models.ForeignKey(User, null=True)

class Item(models.Model):
	taskItem = models.CharField(max_length=255, default="")
	task = models.ForeignKey(Task, null=True, related_name='items')