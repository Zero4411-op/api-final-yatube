from rest_framework.permissions import (
    SAFE_METHODS,
    IsAuthenticatedOrReadOnly,
)


class IsAuthenticatedAuthorOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, content):
        return (
            request.method in SAFE_METHODS
            or content.author == request.user
        )
