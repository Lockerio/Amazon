from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from authentication.permissions import IsOwnerOrReadOnlyLike
from user_advert_relations.models import Like
from user_advert_relations.serializers import LikeSerializer, LikeCreateSerializer, LikeDeleteSerializer


class UserLikesListView(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        # Search by user_id
        user_id = request.GET.get('user_id', None)
        if user_id:
            self.queryset = self.queryset.filter(
                user_id=user_id
            )
        return super().get(request, *args, **kwargs)


class UserLikesCreateView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeCreateSerializer
    permission_classes = [IsAuthenticated]


class UserLikesDeleteView(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeDeleteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyLike]
