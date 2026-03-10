from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet,
)

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
v1_router.register('follow', FollowViewSet, basename='follow')

v1_patterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(v1_patterns)),
]
