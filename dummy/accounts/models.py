from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.deletion import CASCADE

# Create your models here.
class User(AbstractUser):
    DES = (
        ('','Choose Designation'),
        ('admin','Admin/Secretary'),
        ('lecturer','Lecture'),
        ('head of department','Head of Department'),
    )
    is_hod = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    email = models.EmailField( max_length=254)
    designation = models.CharField(max_length=20,choices=DES)
  

    def __str__(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize() +' '+ '('+ self.username +')'

    class Meta:
        ordering = ["-date_joined", ]
