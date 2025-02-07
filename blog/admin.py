from django.contrib import admin
from .models import CustomUser, Post, Comments

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'first_name', 'last_name']

admin.site.register(CustomUser, CustomUserAdmin)  # Only register once
# admin.site.register(Post)
# admin.site.register(Comments)
