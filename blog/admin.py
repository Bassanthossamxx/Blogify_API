from django.contrib import admin
from .models import CustomUser, Post, Comment

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'first_name', 'last_name']

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Post)
# admin.site.register(Comments)
