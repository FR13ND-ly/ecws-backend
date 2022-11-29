from django.db import models
from django.utils import timezone

class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(blank=False, null=False)
    date = models.DateTimeField(default=timezone.now)
    downloaded = models.BooleanField(default=False)
    def __str__(self):
        return self.file.name