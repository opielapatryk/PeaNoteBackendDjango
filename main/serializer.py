from .models import User, Sticker
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'friends','friends_requests','isPrivate', 'askBeforeStick', 'stickersOnBoard', 'pending']

class StickerSerialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sticker
        fields = ['id', 'content', 'creator','timestamp']

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value