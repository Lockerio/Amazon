from django.urls import path
from user_advert_relations.views import UserLikesCreateView, UserLikesDeleteView, UserLikesListView

urlpatterns = [
    path('', UserLikesListView.as_view(), name='user-likes'),
    path('create/', UserLikesCreateView.as_view(), name='user-like-create'),
    path('<int:pk>/delete/', UserLikesDeleteView.as_view(), name='user-like-delete'),
]

if __name__ == '__main__':
    pass
