from rest_framework import serializers
from members.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__' # TODO: setup permissions you dumb cunt (BEFORE USE)