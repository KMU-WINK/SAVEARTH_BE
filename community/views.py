from .models import Board, Comment, Liked
from .serializers import BoardSerialier, CommentSerializer, LikedSerialier
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

class BoardViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
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

class LiketViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Liked.objects.all()
    serializer_class = LikedSerialier

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    def perform_create(self, serializer):
        board = Board.objects.get(id=self.request.data['like_posts'])
        liked_list = Liked.objects.all()
        TorF = True
        for i in liked_list:
            if int(i.user_id) == int(self.request.data['user']):
                if int(i.like_posts_id) == int(self.request.data['like_posts']):
                    TorF = False
                    board.like_down()
                    board.save()
                    i.delete()
                    break
                else:
                    pass
            else:
                pass
        if TorF == True:
            board.like_up()
            board.save()
            serializer.save(user = self.request.user)