""" Custom Permissions for Views """


from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Check if the current logged in user is the owner of the object """

    def has_object_permission(self, request, view, obj):
        """ Check the owner of the object """

        return obj.user == request.user
