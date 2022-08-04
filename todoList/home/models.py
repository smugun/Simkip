from django.db import models


# Create your models here.


class Task(models.Model):
    objects = None
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    complete = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle



