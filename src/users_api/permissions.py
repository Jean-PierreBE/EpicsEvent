from rest_framework import permissions


class OnlyGes(permissions.BasePermission):
    """Allow user to edit with role = 'GES' """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
                return True

        if request.user.role == 'GES':
            return True

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
                return True

        if request.user.role == 'GES':
                return True
