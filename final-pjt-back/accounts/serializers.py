from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'nickname', 'like_genres', 'like_movies', 'reviews', 'profile_image', 'phone_number',
        )
