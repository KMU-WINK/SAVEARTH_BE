from .models import Trashcan
from .serializers import TrashcanSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TrashcanViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)