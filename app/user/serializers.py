from rest_framework import serializers


class SystemUserLoginSerializer(serializers.Serializer):
    """Normal serializer which accepts the email and password"""
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=16, min_length=6, required=True)

    class Meta:
        fields = ("email", "password")
