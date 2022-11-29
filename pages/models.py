from django.db import models
from django.utils import timezone

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(blank=False, null=False)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.file.name
