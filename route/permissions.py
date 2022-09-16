from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # IsOwnerOrReadOnly - 작성자만 접근 or 작성자가 아닌 이는 읽기만 가능
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        # 요청 들어온 method 확인하고 get, head, options 중 하나면 접근 허용

        return object.user == request.user
        # 위의 세개가 아니라면 데이터 유저와 요청한 유저가 같은지 확인하고 결과 리턴
