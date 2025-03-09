from rest_framework import permissions

class IsCustomerAccessible(permissions.BasePermission):
    """
    Allows access only if the customer is assigned to the current user.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.assigned_collection_officer == request.user
