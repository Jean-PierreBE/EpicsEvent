from rest_framework import permissions
from django.shortcuts import get_object_or_404
from events.models import Customer, Contract


class UpdEvent(permissions.BasePermission):
    """Allow user to edit with role = 'COM' """

    def has_permission(self, request, view):
        print('has_permission')
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            parent_contract = get_object_or_404(Contract, pk=view.kwargs['contract_id'])
            parent_customer = get_object_or_404(Customer, pk=parent_contract.customer_id)
            if parent_customer.author_user == request.user and request.user.role == 'COM':
                return True
            else:
                return False
        else:
            return True

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == 'GES':
            return True
        elif request.user.role == 'SUP' and request.user == obj.support_user:
            return True
        else:
            return False
