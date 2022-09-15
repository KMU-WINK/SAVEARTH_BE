from .models import Trash
from .serializers import TrashSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class TrashViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Trash.objects.all()
    serializer_class = TrashSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)