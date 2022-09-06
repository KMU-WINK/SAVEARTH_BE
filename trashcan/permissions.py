from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        # 조회 요청은 true
        if request.method in permissions.SAFE_METHODS:
            return True
        # put, delete요청은 작성자만 허용
        return object.user == request.user