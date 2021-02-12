from django.db import models

# Create your models here.

class MemeModel(models.Model):
     name = models.CharField(max_length=512,null=False)
     url = models.CharField(max_length=512,null=False)
     caption = models.CharField(max_length=512,null=False)
     timestamp = models.DateTimeField(auto_now_add=True, blank=True)
