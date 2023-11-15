from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from advert.models import Advert
from advert.serializers import AdvertListSerializer, AdvertDetailSerializer, AdvertCreateSerializer,\
     AdvertUpdateSerializer, AdvertDeleteSerializer
from authentication.permissions import IsOwnerOrReadOnlyAdvert


class AdvertListView(ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertListSerializer

    def get(self, request, *args, **kwargs):
        # Search by title
        advert_title = request.GET.get('title', None)
        if advert_title:
            self.queryset = self.queryset.filter(
                title__icontains=advert_title
            )

        # Search by tag
        tag_name = request.GET.get('tag', None)
        if tag_name:
            self.queryset = self.queryset.filter(
                tags__name__icontains=tag_name
            )

        self.queryset = self.queryset.order_by('-author_id__is_premium_user', 'title')

        return super().get(request, *args, **kwargs)


class AdvertRetrieveView(RetrieveAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertDetailSerializer


class AdvertCreateView(CreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user)


class AdvertUpdateView(UpdateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyAdvert]


class AdvertDeleteView(DestroyAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertDeleteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyAdvert]
