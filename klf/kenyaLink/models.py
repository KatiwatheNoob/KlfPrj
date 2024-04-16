

# Create your models here.
from django.db import models
import datetime

class ContactSubmission(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    subject = models.CharField(max_length=256)
    message = models.TextField()
    agree_to_terms = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.subject}'
