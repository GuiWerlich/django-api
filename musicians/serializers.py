from rest_framework import serializers
from musicians.models import Musician

class MusicianSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    instrument = serializers.CharField()

    def create(self, validated_data):
        return Musician.objects.create(**validated_data)