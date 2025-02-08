from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import egyptian_phone_validator

#User :
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(
        max_length=11,
        validators=[egyptian_phone_validator],
        # unique=True, will try it
        null=False,
        blank=False,)
    def __str__(self):
        return self.username



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.title



class Comments(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)