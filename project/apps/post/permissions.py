from rest_framework import permissions
from apps.user.models import UserModel


class IsVisitorUser(permissions.BasePermission):
    message = "Only Visitor user can leave a comment"

    def has_permission(self, request, view):
        """ check is request user is "Visitor" user """
        try:
            visitor = request.user.visitormodel
            return True
        except UserModel.visitormodel.RelatedObjectDoesNotExist:
            return False
