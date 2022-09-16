from .models import Trashcan
from .serializers import TrashcanSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class TrashcanViewSet(viewsets.ModelViewSet):
    # ModelViewSet - 자동으로 CRUD를 구축해주는 클래스를 받아와서 사용
    authentication_classes = [TokenAuthentication]
    # Trashcan api 사용자 신원을 인증하고 CRUD권한을 주기 전 Token을 헤더로 받아서 확인하겠다는 코드
    permission_classes = [IsAuthenticated]
    # 로그인한 사용자라면 누구에게나 CRUD 할 수 있는 권한을 주겠다는 코드
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer
    # 앞서 설정한 TrashcanSerializer를 api의 serializer로 설정

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    # modelViewSet의 perform_create 오버라이딩
    # POST메소드 사용시 실행 - 데이터 생성할 때 request를 요청한 user의 id로 자동 저장