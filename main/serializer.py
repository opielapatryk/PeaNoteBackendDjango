from .models import User, Sticker
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'friends','isPrivate', 'askBeforeStick', 'stickersOnBoard']

class StickerSerialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sticker
        fields = ['id', 'content', 'creator','timestamp']