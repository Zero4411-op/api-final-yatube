from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post
from .permissions import IsAuthenticatedAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class AuthorContentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedAuthorOrReadOnly,)


class PostViewSet(AuthorContentViewSet):
    queryset = Post.objects.select_related(
        'author',
        'group',
    )
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(AuthorContentViewSet):
    serializer_class = CommentSerializer

    def get_post(self):
        return get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id'),
        )

    def get_queryset(self):
        return self.get_post().comments.select_related(
            'author',
            'post',
        )

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post(),
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follows.select_related(
            'user',
            'following',
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
