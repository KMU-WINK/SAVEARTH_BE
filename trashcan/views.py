from .models import Trashcan
from .serializers import TrashcanSerializer
from rest_framework import viewsets

class TrashcanViewSet(viewsets.ModelViewSet):
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer
