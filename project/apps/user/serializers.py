from rest_framework import serializers
from apps.user.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = ("first_name", "last_name", "email", "photo", "full_name")

    def get_full_name(self, obj):
        return str(obj)