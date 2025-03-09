from rest_framework import permissions

class IsCallingAgent(permissions.BasePermission):
    """
    Allows access only to users with the 'calling_agent' role.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'calling_agent'
    
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.role == 'calling_agent' and obj.interaction_type == 'calling'

class IsFieldOfficer(permissions.BasePermission):
    """
    Allows access only to users who are NOT calling agents.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role != 'calling_agent'
    
    def has_object_permission(self, request, view, obj):
        return obj.interaction_type == 'field' and obj.loan.customer.assigned_collection_officer == request.user
