from .models import Board, Comment, Liked
from .serializers import BoardSerialier, CommentSerializer, LikedSerialier
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action

class BoardViewSet(viewsets.ModelViewSet):   # ModelViewSet - 자동으로 CRUD를 구축해주는 클래스를 받아와서 사용
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerialier

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'board_id'

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        cntUp = Board.objects.get(id=self.request.data['board'])
        cntUp.comment_up()
        cntUp.save() 
    # Comment가 생성 될 때 입력된 Board_id를 확인해서 해당 Board의 comment_up함수를 이용해 comment_cnt를 증가

    @action(detail=False, methods=["get"], url_path=r"(?P<board_id>\w+)")
    def public_list(self, request, board_id=None):
        qs = self.queryset.filter(board_id=board_id)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    # 기존 endpoint는 community/comment/<comment_id>/ 이지만 community/comment/<board_id>/ 로변경

class LiketViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Liked.objects.all()
    serializer_class = LikedSerialier

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
    # JSON타입으로 입력 받은 user_id 와 like_post가 같은 인스턴스가 존재한다면 그 인스턴스를 지우고 Board의
    # like_down함수를 이용해 like_cnt 감소, user_id, like_post가 하나라도 다르다면 Comment를 생성하고
    # Board의 like_up 함수를 이용해 like_cnt 증가
