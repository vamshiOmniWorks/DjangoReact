from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_type = models.TextField()
    created_by = models.TextField()
    created_on = models.DateTimeField()
    modified_on = models.DateTimeField(null=True)
    modified_by = models.TextField(null=True)
