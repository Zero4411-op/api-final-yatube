from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet
)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'v1/posts/<int:post_id>/comments/',
        comments_list,
        name='comments-list'
    ),
    path(
        'v1/posts/<int:post_id>/comments/<int:pk>/',
        comments_detail,
        name='comments-detail'
    ),
]
