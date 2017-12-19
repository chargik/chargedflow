from django.db import models
from pages.models import Tours

# Create your models here.
class Join(models.Model):
    lead_name = models.CharField(max_length=128)
    telephone = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.lead_name


    def save(self, *args, **kwargs):
        super(Join, self).save(*args, **kwargs) 