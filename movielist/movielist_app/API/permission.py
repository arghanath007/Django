from rest_framework import permissions


class isAdminOrReadOnly(permissions.IsAdminUser):

    """Checking to see if the user has Admin permissions or not. If the user is an Admin or not. If the user is Admin, we need to return True otherwise return false. The Admin has access to DELETE, PUT and POST methods. The normal or not logged in user has access to GET method only or Read only."""

    # def has_permission(self, request, view):
    # adminPermission = super().has_permission(request, view)
    #     adminPermission = bool(request.user and request.user.is_staff)
    #     return request.method == 'GET' or adminPermission

    # 'has_object_permission()', here we are specifically checking a particular object. So an individual review object can be edited by it's own owner only.

    # 'has_permission()', We are generally checking if the user has permission to read or anything else.

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        else:

            # If the user is Admin, then return True as well.
            return bool(request.user and request.user.is_staff)


class IsReviewerOrAdminOtherwiseReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # 'SAFE_METHODS' is 'GET' request.
            return True
        else:
            # We are checking if the 'reviewer'(obj.reviewer) is the same as the currently logged in user(request.user) or if the logged in user is an 'Admin', then we are returning True. Otherwise return false.
            return obj.reviewer == request.user or request.user.is_staff
