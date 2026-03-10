from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class AuthorSerializerMixin(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        abstract = True


class PostSerializer(AuthorSerializerMixin):

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(AuthorSerializerMixin):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны.',
            ),
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        return representation

    def validate_following(self, following_user):
        current_user = self.context['request'].user

        if current_user == following_user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )

        return following_user
