from django.db import models

import uuid

class User(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=False)
    family_name = models.CharField(max_length=200, blank=False)
    institution = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return self.name

class Predictions(models.Model):

    id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    model_name = models.CharField(max_length=200, blank=False)
    score = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.BinaryField()

    def __str__(self):
        return self.results

