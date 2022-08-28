from rest_framework import permissions


class IsArticleEditableOrDestroyable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and (request.user == obj.writer or request.user.is_staff)
