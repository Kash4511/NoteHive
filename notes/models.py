from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the note to a specific user
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Adds a timestamp for when the note was created

    def __str__(self):
        return self.title