from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateField()
    amout = models.FloatField()
    status = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

