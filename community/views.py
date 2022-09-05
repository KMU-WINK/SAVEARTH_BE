from .models import Board, Comment
from .serializers import BoardSerialier, CommentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action

class BoardViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerialier

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'board_id'

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        cntUp = Board.objects.get(id=self.request.data['board'])
        cntUp.comment_up()
        cntUp.save()

    @action(detail=False, methods=["get"], url_path=r"(?P<board_id>\w+)")
    def public_list(self, request, board_id=None):
        qs = self.queryset.filter(board_id=board_id)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)