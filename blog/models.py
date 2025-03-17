from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import egyptian_phone_validator

#User :
#Customize User :
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=65,blank=False , null=False)
    last_name = models.CharField(max_length=65,blank=False , null=False)
    phone = (models.CharField
             (max_length=11,
              validators=[egyptian_phone_validator],
              blank=False,
              null=True,
              unique=True))
    def __str__(self):
        return self.username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone' , 'first_name','last_name','username']


# Posts table
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


# Comments table
class Comments(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)