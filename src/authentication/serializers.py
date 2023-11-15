from django.urls import reverse
from rest_framework import serializers
from authentication.models import User


class UserListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = ["id", "username", "photo", "url"]


class UserDetailSerializer(serializers.ModelSerializer):
    likes_url = serializers.SerializerMethodField()

    def get_likes_url(self, obj):
        return f'{reverse("user-likes")}?user_id={obj.pk}'

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "phone_number", "photo",
                  "is_premium_user", "likes_url"]


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "first_name",
                  "last_name", "phone_number", "photo", "password"]

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "phone_number", "photo"]


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
