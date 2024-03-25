from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    street = serializers.CharField()
    house_number = serializers.CharField()
    city = serializers.CharField()
    zip_code = serializers.CharField()

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    sex = serializers.CharField()
    addresses = AddressSerializer(many=True)