from rest_framework import permissions

from apps.general.models import General


class CheckUserBalance(permissions.BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'balance', 0) >= General.get_booking_price()