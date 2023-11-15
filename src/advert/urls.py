from django.urls import path

from advert.views import AdvertListView, AdvertRetrieveView, AdvertCreateView, AdvertDeleteView, AdvertUpdateView


urlpatterns = [
    path('', AdvertListView.as_view(), name='advert-list'),
    path('create/', AdvertCreateView.as_view(), name='advert-create'),
    path('<int:pk>/', AdvertRetrieveView.as_view(), name='advert-detail'),
    path('<int:pk>/update/', AdvertUpdateView.as_view(), name='advert-update'),
    path('<int:pk>/delete/', AdvertDeleteView.as_view(), name='advert-delete'),
]


if __name__ == '__main__':
    pass
