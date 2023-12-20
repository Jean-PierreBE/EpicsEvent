from rest_framework import permissions


class OnlyCom(permissions.BasePermission):
    """Allow user to edit with role = 'COM' """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == 'COM':
            return True

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == 'COM':
            return True
