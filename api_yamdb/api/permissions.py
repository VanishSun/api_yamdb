from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_superuser
            or request.user.is_admin
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_superuser
            or request.user.is_admin
        )