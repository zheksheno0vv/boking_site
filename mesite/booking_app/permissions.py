from rest_framework import permissions


class CheckCreateHotel(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return True
        return False


