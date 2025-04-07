from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only for others
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the author can update/delete
        return obj.author == request.user
