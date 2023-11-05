from rest_framework import permissions
from django.shortcuts import get_object_or_404
from events.models import Customer


class UpdContract(permissions.BasePermission):
    """Allow user to edit with role = 'COM' """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == 'GES':
            return True

        parent_customer = get_object_or_404(Customer, pk=view.kwargs['customer_id'])
        if parent_customer.author_user == request.user:
            if request.method == 'POST':
                return False
            else:
                return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        print('debut')
        if request.method in permissions.SAFE_METHODS:
            return True
        parent_customer = get_object_or_404(Customer, pk=view.kwargs['customer_id'])

        if request.user.role == 'GES':
            return True
        elif parent_customer.author_user == request.user:
            return True
        else:
            return False
