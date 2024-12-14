from django.db import models
from django.utils import timezone

class varity(models.Model):
    Choice = [
        ('SH', 'Shoe'),
        ('CL', 'Cloths'),
        ('WT', 'Watch'),

    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='app')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=Choice)
    def __str__(self):
        return self.name

