from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body