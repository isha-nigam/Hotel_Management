from django.db import models

# Create your models here.

class receptionist(models.Model):
    ruser = models.CharField(max_length=50)
    rname = models.CharField(max_length=50)
    rmail = models.CharField(max_length=50)
    rcontact = models.CharField(max_length=50)
    rpass = models.CharField(max_length=50)
    
    def __str__(self):
        return self.ruser

class guest_entries(models.Model):
    guest_name = models.CharField(max_length=50)
    guest_num = models.CharField(max_length=50)
    guest_id = models.CharField(max_length=50)
    guest_room = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    intime = models.CharField(max_length=50)
    exittime = models.CharField(max_length=50)
    
    def __str__(self):
        return self.guest_name
