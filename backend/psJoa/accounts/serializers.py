from .models import CustomUser
from rest_framework import serializers

class MyInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class YourInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'