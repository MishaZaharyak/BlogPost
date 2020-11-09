from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """ Login serializer """
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)