from rest_framework import serializers
from apps.user.models import UserModel, VisitorModel


class UserSerializer(serializers.ModelSerializer):
    """ Admin user serializer """
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = ('id', "first_name", "last_name", "email", "photo", "full_name")

    def get_full_name(self, obj):
        return str(obj)


class VisitorSerializer(UserSerializer):
    """ Visitor user serializer """
    class Meta:
        model = VisitorModel
        fields = ("first_name", "last_name", "email", "photo", "full_name")
