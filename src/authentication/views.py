from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from authentication.permissions import IsOwnerOrReadOnlyUser
from authentication.serializers import UserListSerializer, UserCreateSerializer, UserDetailSerializer, \
     UserUpdateSerializer, UserDeleteSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        # Search by username
        username_text = request.GET.get('username', None)
        if username_text:
            self.queryset = self.queryset.filter(
                username__icontains=username_text
            )

        self.queryset = self.queryset.order_by('-is_premium_user', 'last_name')

        return super().get(request, *args, **kwargs)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyUser]


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyUser]
