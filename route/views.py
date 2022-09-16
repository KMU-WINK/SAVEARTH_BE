from .models import Route
from .serializers import RouteSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from route.permissions import IsOwnerOrReadOnly

class RouteViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # 위에서 정의한 IsOwnerOrReadOnly 추가 - 권한 접근 추가
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']
    # 필터링 할 필드 정함(나의 운동 기록을 봐야하기 때문에 사용자 아이디를 필터링 해야함)
    # serializer에서 user를 user_id로 해놨기 때문에 user_id를 검색할 필드 이름으로 정함
    # user_id가 json으로 보일 땐 닉네임으로 보이지만 실제 값은 user데이터의 id값이기 때문에 숫자로 검색해줘야함.

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)