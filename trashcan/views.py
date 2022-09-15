from .models import Trashcan
from .serializers import TrashcanSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class TrashcanViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    