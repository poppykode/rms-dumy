from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.deletion import CASCADE

# Create your models here.
class User(AbstractUser):
    email = models.EmailField( max_length=254)
    designation = models.CharField(max_length=20,default="chief records officer")
  

    def __str__(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize() +' '+ '('+ self.username +')'

    class Meta:
        ordering = ["-date_joined", ]
