from .models import Trashcan
from .serializers import TrashcanSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class TrashcanViewSet(viewsets.ModelViewSet):
    # csrftoken 사용시 아래 두 코드 풀기
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id', 'trashcan_x', 'trashcan_y']

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    