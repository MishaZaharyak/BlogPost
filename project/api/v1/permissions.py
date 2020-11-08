from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    message = "Only for admin users"

    def has_permission(self, request, view):
        return request.user.is_superuser
