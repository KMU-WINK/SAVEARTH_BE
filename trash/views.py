from .models import Trash
from .serializers import TrashSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class TrashViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Trash.objects.all()
    serializer_class = TrashSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id','trash_x','trash_y']

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)