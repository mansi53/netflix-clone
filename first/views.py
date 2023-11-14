from rest_framework import viewsets,serializers

from django.contrib.auth.models import User

MIN_LENGTH= 8


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        default_error_messages={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    password2=serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        default_error_messages={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("password does not match")
            return super().validate(data)