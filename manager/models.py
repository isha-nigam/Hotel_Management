from django.db import models

# Create your models here.

class manager_login(models.Model):
    muser = models.CharField(max_length=50)    
    mpass = models.CharField(max_length=50)
    
    def __str__(self):
        return self.muser